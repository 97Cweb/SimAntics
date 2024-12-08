import threading
import time

class ClientConnection:
    def __init__(self, username):
        self.username = username
        self.client_socket = None  # Tracks connected client
        self.udp_address = None
        self.lock = threading.Lock()  # Synchronize access if needed
        self.last_active = time.time()  # Track last active time

    
    def update_last_active(self):
        """Update the last active timestamp."""
        self.last_active = time.time()