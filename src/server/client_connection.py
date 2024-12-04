import threading

class ClientConnection:
    def __init__(self, username):
        self.username = username
        self.client_socket = None  # Tracks connected client
        self.lock = threading.Lock()  # Synchronize access if needed

    def assign_client_socket(self, client_socket):
        """Assign a client socket to this player."""
        with self.lock:
            self.client_socket = client_socket

    def remove_client_socket(self):
        """Remove the client socket from this player."""
        with self.lock:
            self.client_socket = None