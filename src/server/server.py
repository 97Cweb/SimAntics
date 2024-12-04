import socket
import threading
import json5

from client_connection import ClientConnection


class Server(threading.Thread):
    def __init__(self, host='127.0.0.1', port=65432):
        super().__init__()
        self.host = host
        self.port = port
        self.server_socket = None
        self.running = False
        self.connected_clients = {} #username -> client_connection


    def authenticate(self, credentials):
        """Authenticate client"""
        password = credentials.get("password")
        if password == "pw":
            return True
        return False
    
    
    def handle_connection(self, client_socket):
       """Authenticate clients and associate them with players."""
       try:
           data = client_socket.recv(1024).decode('utf-8')
           credentials = json5.loads(data)

           if self.authenticate(credentials):
               username = credentials.get("username")
               client_connection = self.connected_clients[username] = ClientConnection(username)
               client_connection.assign_client_socket(client_socket)
               print(f"client {username} authenticated and connected.")
           else:
               client_socket.sendall(json5.dumps({"status": "error", "message": "Authentication failed"}).encode('utf-8'))
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

        while self.running:
            try:
                client_socket, client_address = self.server_socket.accept()
                print(f"New connection from {client_address}")
                client_thread = threading.Thread(target=self.handle_connection, args=(client_socket,))
                client_thread.start()
            except socket.timeout:
                continue  # Timeout allows the loop to check the `running` flag

    def stop(self):
        """Stop the server."""
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        print("Server stopped.")


