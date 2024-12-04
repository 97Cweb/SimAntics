import socket
import json5
import threading
import time

HOST = '127.0.0.1'
PORT = 65432
KEEP_ALIVE_INTERVAL = 5  # Seconds

def send_keep_alive(client):
    """Send keep-alive messages periodically."""
    while True:
        try:
            time.sleep(KEEP_ALIVE_INTERVAL)
            message = json5.dumps({"type": "keep_alive"})
            client.sendall(message.encode('utf-8'))
        except (ConnectionResetError, BrokenPipeError, ConnectionAbortedError):
            print("Disconnected from server.")
            break


def main():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORT))
        print("Connected to server.")

        message = json5.dumps({"username": "cb", "password": "pw"})
        client.sendall(message.encode('utf-8'))

        # Receive response
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
        
        # Start keep-alive thread
        keep_alive_thread = threading.Thread(target=send_keep_alive, args=(client,), daemon=True)
        keep_alive_thread.start()
        
        # Simulate other client actions
        while keep_alive_thread.is_alive():
            time.sleep(0.1)  # Replace with actual client logic
    except KeyboardInterrupt:
        print("Stopping client...")
    except Exception as e:
        print(f"Client error: {e}")
    finally:
        # Ensure resources are cleaned up
        if keep_alive_thread:
            keep_alive_thread.join()  # Wait for the keep-alive thread to finish
        if client:
            client.close()
        print("Client has stopped.")

if __name__ == "__main__":
    main()
