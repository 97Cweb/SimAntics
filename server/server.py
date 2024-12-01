import socket
import threading
from handlers.client_handler import handle_client
from simulation import simulation_instance

class Server(threading.Thread):
    def __init__(self, host='127.0.0.1', port=65432):
        super().__init__()
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False

    def run(self):
        """Start the server loop."""
        self.running = True
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.server_socket.settimeout(1.0)  # Non-blocking with 1-second timeout
        print(f"Server listening on {self.host}:{self.port}")

        while self.running:
            try:
                client_socket, client_address = self.server_socket.accept()
                print(f"New connection from {client_address}")
                client_thread = threading.Thread(target=handle_client, args=(client_socket,))
                client_thread.start()
            except socket.timeout:
                continue  # Timeout allows the loop to check the `running` flag

    def stop(self):
        """Stop the server."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        print("Server stopped.")
