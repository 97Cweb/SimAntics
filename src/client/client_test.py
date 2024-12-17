import socket
import json5
import threading
import time


class Client:
    def __init__(self, host='127.0.0.1', tcp_port=65432, udp_port=65433, keep_alive_interval=5):
        self.host = host
        self.tcp_port = tcp_port
        self.udp_port = udp_port
        self.keep_alive_interval = keep_alive_interval

        self.tcp_client = None
        self.udp_socket = None
        self.keep_alive_thread = None
        self.udp_thread = None
        self.tcp_thread = None  # New TCP listener thread
        self.running = True
        self.last_frame = 0

    def send_keep_alive(self):
        """Send keep-alive messages periodically."""
        while self.running:
            try:
                time.sleep(self.keep_alive_interval)
                message = json5.dumps({"type": "keep_alive"})
                self.tcp_client.sendall(message.encode('utf-8'))
            except (ConnectionResetError, BrokenPipeError, ConnectionAbortedError):
                print("Disconnected from server.")
                self.running = False
                break

    def listen_for_udp_updates(self):
        """Listen for UDP updates from the server."""
        try:
            while self.running:
                # Receive data from the server
                data, server_address = self.udp_socket.recvfrom(4096)  # Buffer size
                state = json5.loads(data.decode('utf-8'))

                # Process only new frames
                if state["frame"] > self.last_frame:
                    self.last_frame = state["frame"]
                    print(f"Received frame {state['frame']}: {state}")

                    # Send acknowledgment if required
                    if state.get("require_ack"):
                        ack_message = json5.dumps({"type": "ack", "frame": state["frame"]}).encode('utf-8')
                        self.udp_socket.sendto(ack_message, server_address)
                else:
                    print(f"Ignored outdated frame {state['frame']}")
        except Exception as e:
            print(f"Error in UDP listener: {e}")
            
    def listen_for_tcp_messages(self):
        """Listen for TCP messages from the server."""
        buffer = ""  # Buffer to accumulate data
    
        while self.running:
            try:
                data = self.tcp_client.recv(4096).decode('utf-8')
                if not data:
                    print("Disconnected from server.")
                    self.running = False
                    break
    
                buffer += data  # Append new data to the buffer
                
                # Process complete messages
                while "\n" in buffer:
                    message, buffer = buffer.split("\n", 1)
                    try:
                        parsed_message = json5.loads(message)
                        print(f"Received: {parsed_message}")
                    except json5.JSONDecodeError as e:
                        print(f"Failed to parse message: {message}. Error: {e}")
    
            except (ConnectionResetError, BrokenPipeError, ConnectionAbortedError):
                print("Disconnected from server.")
                self.running = False
                break
            except Exception as e:
                print(f"Error in TCP listener: {e}")


    def connect(self, username, password):
        """Connect to the server and start threads."""
        try:
            # Set up UDP socket
            self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_socket.bind((self.host, self.udp_port))

            # Connect to the TCP server
            self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.tcp_client.connect((self.host, self.tcp_port))
            print("Connected to server.")

            # Authenticate with the server
            auth_message = json5.dumps({"username": username, "password": password, "udp_port": self.udp_port})
            self.tcp_client.sendall(auth_message.encode('utf-8'))

            # Receive response
            response = self.tcp_client.recv(1024).decode('utf-8')
            print(f"Server response: {response}")

            # Start UDP listener thread
            self.udp_thread = threading.Thread(target=self.listen_for_udp_updates, daemon=True)
            self.udp_thread.start()

            # Start TCP listener thread
            self.tcp_thread = threading.Thread(target=self.listen_for_tcp_messages, daemon=True)
            self.tcp_thread.start()
            
            # Start keep-alive thread
            self.keep_alive_thread = threading.Thread(target=self.send_keep_alive, daemon=True)
            self.keep_alive_thread.start()

            # Main loop
            print("Client running. Press Ctrl+C to stop.")
            while self.running:
                time.sleep(0.1)  # Replace with actual client logic

        except KeyboardInterrupt:
            print("Stopping client...")
        except Exception as e:
            print(f"Client error: {e}")
        finally:
            self.shutdown()

    def shutdown(self):
        """Shut down the client and clean up resources."""
        self.running = False
        if self.keep_alive_thread and self.keep_alive_thread.is_alive():
            self.keep_alive_thread.join()
        if self.udp_thread and self.udp_thread.is_alive():
            self.udp_thread.join()
        if self.tcp_thread and self.tcp_thread.is_alive():
            self.tcp_thread.join()
        if self.tcp_client:
            self.tcp_client.close()
        if self.udp_socket:
            self.udp_socket.close()
        print("Client has stopped.")


if __name__ == "__main__":
    client = Client()
    client.connect(username="cb", password="pw")
