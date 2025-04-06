import threading
import time
import json5

from steamworks import STEAMWORKS

from network_manager import NetworkManager
class Client:
    def __init__(self, host='127.0.0.1', tcp_port=65432, udp_port=65433, keep_alive_interval=5):
        self.init_steam()
        
        self.network = NetworkManager(host, tcp_port, udp_port)
        self.keep_alive_interval = keep_alive_interval
        self.running = True
        self.last_frame = 0

        self.keep_alive_thread = None
        self.udp_thread = None
        self.tcp_thread = None
        
    def init_steam(self):
        #setup steamworks
        self.steamworks = STEAMWORKS()
        self.steamworks.initialize()
        if (self.steamworks.UserStats.RequestCurrentStats() == True):
            print('Stats successfully retrieved!')

    def connect(self, username, password):
        try:
            # Connect to TCP and UDP
            self.network.connect_tcp()
            self.network.bind_udp()

            # Authenticate
            auth_message = {"username": username, "password": password, "udp_port": self.network.udp_port}
            self.network.send_tcp(auth_message)
            response = self.network.receive_tcp()
            print(f"Server response: {response}")

            # Start threads
            self.keep_alive_thread = threading.Thread(target=self.send_keep_alive, daemon=True)
            self.udp_thread = threading.Thread(target=self.listen_for_udp_updates, daemon=True)
            self.tcp_thread = threading.Thread(target=self.listen_for_tcp_messages, daemon=True)

            self.keep_alive_thread.start()
            self.udp_thread.start()
            self.tcp_thread.start()

            # Main loop
            print("Client running. Press Ctrl+C to stop.")
            #while self.running:
                #time.sleep(0.1)

        except KeyboardInterrupt:
            print("Stopping client...")
        except Exception as e:
            print(f"Client error: {e}")
        finally:
            self.shutdown()

    def send_keep_alive(self):
        """Send keep-alive messages periodically."""
        while self.running:
            try:
                time.sleep(self.keep_alive_interval)
                self.network.send_tcp({"type": "keep_alive"})
            except Exception as e:
                print(f"Keep-alive error: {e}")
                self.running = False

    def listen_for_udp_updates(self):
        """Listen for UDP updates from the server."""
        try:
            while self.running:
                state, server_address = self.network.receive_udp()
                if state["frame"] > self.last_frame:
                    self.last_frame = state["frame"]
                    print(f"Received frame {state['frame']}: {state}")
                else:
                    print(f"Ignored outdated frame {state['frame']}")
        except Exception as e:
            print(f"UDP listener error: {e}")

    def listen_for_tcp_messages(self):
        """Listen for TCP messages from the server."""
        buffer = ""
        while self.running:
            try:
                data = self.network.receive_tcp()
                buffer += data
                while "\n" in buffer:
                    message, buffer = buffer.split("\n", 1)
                    print(f"Received: {json5.loads(message)}")
            except Exception as e:
                print(f"TCP listener error: {e}")
                self.running = False

    def shutdown(self):
        print("in shutdown")
        """Shut down the client."""
        self.running = False
        self.network.close()
        
        if self.keep_alive_thread is not None:
            self.keep_alive_thread.join(timeout=2)
        if self.udp_thread is not None:
            self.udp_thread.join(timeout=2)
        if self.tcp_thread is not None:
            self.tcp_thread.join(timeout=2)
        
        self.steamworks.unload()
        del self.steamworks
        print("Client has stopped.")
