import base64
import io
import json5
import os
import shutil
import socket
import threading
import time
import zipfile


from queue import Queue

from client_connection import ClientConnection
from message_throttler import MessageThrottler


class Server(threading.Thread):
    def __init__(self, simulation, host='127.0.0.1', port=65432, udp_port=65433, inactivity_timeout=15, message_interval_rate = 5):
        super().__init__()
        self.simulation = simulation
        self.host = host
        self.port = port
        self.udp_port = udp_port
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket = None
        self.running = False
        self.connected_clients = {} #username -> client_connection
        self.inactivity_timeout = inactivity_timeout
        
        self.outbound_queue = Queue()
        
        # Track unacknowledged frames
        self.unacknowledged_frames = {}  # {client_address: {frame: (timestamp, state)}}

        self.message_throttler = MessageThrottler(send_callback=self.send_message_to_client, interval= message_interval_rate)

        self.upload_buffers = {}  # username -> bytearray


    def authenticate(self, credentials):
        """Authenticate client"""
        password = credentials.get("password")
        if password == "a":
            return True
        return False
    
    
    def listen_for_client_messages(self, username):
        """Continuously listen for messages from the client."""
        client_connection = self.connected_clients[username]
        while self.running:
            try:
                data = client_connection.client_socket.recv(1024).decode('utf-8')
                if not data:
                    break  # Connection closed
                message = json5.loads(data)
                if message.get("type") == "keep_alive":
                    # Update the client's last active time
                    client_connection.last_active = time.time()
                    print(f"Keep-alive received from {username}")
                    
                elif message.get("type") == "file_upload":
                    self.handle_file_upload(username, message)
                else:
                    print(f"Unhandled message type from {username}: {message['type']}")
            except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
                break
            except Exception as e:
                print(f"Error processing message from {username}: {e}")
                break
        # Disconnect client if the loop exits
        self.disconnect_client(username)

    
    def handle_connection(self, client_socket):
       """Authenticate clients and associate them with players."""
       try:
           data = client_socket.recv(1024).decode('utf-8')
           credentials = json5.loads(data)

           if self.authenticate(credentials):
               username = credentials.get("username")
               udp_port = credentials["udp_port"]
               client_connection = self.connected_clients[username] = ClientConnection(username)
               client_connection.client_socket = client_socket
               client_connection.udp_address = (client_socket.getpeername()[0], udp_port)
               print(f"client {username} authenticated and connected.")
               message = {
                   "status": "success", 
                   "message": "Authentication succeeded",
                   "server_id":self.simulation.simulation_config["server_id"]
                   }
               self.send_json_line(client_socket, message)
               # Notify simulation of the new player
               self.notify_simulation(event="login", username=username)
                
               # Start a thread to listen for client messages
               threading.Thread(target=self.listen_for_client_messages, args=(username,), daemon=True).start()
           else:
               self.send_json_line(client_socket,{"status": "error", "message": "Authentication failed"})
               client_socket.close()
       except Exception as e:
           print(f"Error during authentication: {e}")
           client_socket.close()
    
    
    
    def run(self):
        """Start the server loop."""
        self.running = True
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.server_socket.settimeout(1.0)  # Non-blocking with 1-second timeout
        print(f"Server listening on {self.host}:{self.port}")

        threading.Thread(target=self.heartbeat_monitor, daemon=True).start()
        
        # Start a thread for UDP broadcasting
        threading.Thread(target=self.broadcast_updates, daemon=True).start()
        
        while self.running:
            try:
                client_socket, client_address = self.server_socket.accept()
                print(f"New connection from {client_address}")
                client_thread = threading.Thread(target=self.handle_connection, args=(client_socket,))
                client_thread.start()
            except socket.timeout:
                continue  # Timeout allows the loop to check the `running` flag
            
            except OSError:
                # Gracefully handle the case where the socket is closed
                if not self.running:
                    break  # Exit the loop if the server is no longer running

    def stop(self):
        """Stop the server."""
        self.running = False
        self.message_throttler.stop()
        try:
            if self.server_socket:
                self.server_socket.close()
                self.server_socket = None
            if self.udp_socket:
                self.udp_socket.close()
                self.udp_socket = None
            print("Server stopped.")
        except OSError as e:
            print(f"Error while stopping server: {e}")
        
    def broadcast_updates(self):
        """Process the outbound queue and send updates via UDP."""
        while self.running:
            try:
                # Send queued updates
                while not self.outbound_queue.empty():
                    state = self.outbound_queue.get()
                    self.send_state_to_clients(state, require_ack=False)

                # Retransmit unacknowledged frames
                current_time = time.time()
                for client_address, frames in list(self.unacknowledged_frames.items()):
                    for frame, (timestamp, state) in list(frames.items()):
                        if current_time - timestamp > 1.0:  # Retransmit after 1 second
                            print(f"Retransmitting frame {frame} to {client_address}")
                            self.udp_socket.sendto(json5.dumps(state).encode('utf-8'), client_address)
                            self.unacknowledged_frames[client_address][frame] = (current_time, state)
                time.sleep(0.01)  # prevents tight loop and CPU hogging

            except Exception:
                pass  # Handle timeout or empty queue
                    
    def send_state_to_clients(self, state, require_ack=False):
        """Send simulation state to all clients."""
        state["require_ack"] = require_ack  # Add acknowledgment flag
        message = json5.dumps(state).encode('utf-8')

        for client in self.connected_clients.values():
            if client.udp_address:
                self.udp_socket.sendto(message, client.udp_address)

                # Track unacknowledged frames if required
                if require_ack:
                    if client.udp_address not in self.unacknowledged_frames:
                        self.unacknowledged_frames[client.udp_address] = {}
                    self.unacknowledged_frames[client.udp_address][state["frame"]] = (time.time(), state)


    def send_message_to_client(self, username, message):
        client_connection = self.connected_clients.get(username)
        if client_connection:
            self.send_json_line(client_connection.client_socket, {
                "type": "message",
                "content": message
            })
        else:
            print(f"[Warning] Attempted to send message to {username}, but they are not connected.")

        
        


    def handle_file_upload(self, username:str, message):
        try:
            chunk_index = message["chunk_index"]
            total_chunks = message["total_chunks"]
            chunk_data = base64.b64decode(message["payload"])
            buf = self.upload_buffers.setdefault(username, bytearray())
            buf.extend(chunk_data)
    
            if chunk_index == total_chunks - 1:
                print(f"Received all {total_chunks} chunks from {username}")
                # Extract zip
                player = self.simulation.players.get(username)
                if not player:
                    raise ValueError(f"Player {username} not found.")
                player_folder = os.path.join("saves", player.save_name, "players", str(username))
    
                if os.path.exists(player_folder):
                    shutil.rmtree(player_folder)
                os.makedirs(player_folder, exist_ok=True)
    
                with zipfile.ZipFile(io.BytesIO(buf)) as zipf:
                    zipf.extractall(player_folder)
    
                del self.upload_buffers[username]
    
                print(f"Unpacked upload for {username} to {player_folder}")
                player._initialize_lua_environment()
                
                self.send_json_line(
                    self.connected_clients[username].client_socket,
                    {"status": "success", "message": f"Upload complete for {username}."}
                )

        except Exception as e:
            print(f"Error during file upload for {username}: {e}")
            self.send_json_line(
                self.connected_clients[username].client_socket,
                {"status": "error", "message": str(e)}
            )


    def notify_simulation(self, event, username):
        self.simulation.command_queue.put({
            "event":event,
            "username":username
            })

    def disconnect_client(self, username):
        """Handle client disconnection."""
        if username in self.connected_clients:
            client = self.connected_clients.pop(username, None)
            if client and client.udp_address in self.unacknowledged_frames:
                del self.unacknowledged_frames[client.udp_address]
            print(f"Client {username} disconnected.")

    def heartbeat_monitor(self):
        """Check for inactive clients periodically."""
        while self.running:
            time.sleep(5)  # Check every 5 seconds
            current_time = time.time()
            for username, client_connection in list(self.connected_clients.items()):
                if (current_time - client_connection.last_active) > self.inactivity_timeout:
                    print(f"Client {username} timed out due to inactivity.")
                    self.notify_simulation("logout", username)
                    self.disconnect_client(username)
                    
    def send_json_line(self, socket_obj, data):
        """Helper to send JSON with newline terminator."""
        try:
            message = json5.dumps(data) + "\n"
            socket_obj.sendall(message.encode("utf-8"))
        except Exception as e:
            print(f"[Error] Failed to send message: {e}")

                    
