import socket
import threading
from handlers.client_handler import handle_client
from simulation import simulation_instance

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

def start_server():
    # Start the simulation
    simulation_instance.start()

    # Set up the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")

    try:
        while True:
            client_socket, client_address = server.accept()
            print(f"New connection from {client_address}")
            client_thread = threading.Thread(target=handle_client, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("Shutting down server...")
        simulation_instance.stop()
        server.close()

if __name__ == "__main__":
    start_server()
