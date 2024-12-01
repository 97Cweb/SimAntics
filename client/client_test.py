import socket
import json

HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("Connected to server.")

        # Send a test message
        message = json.dumps({"command": "run_script", "script": "print('Hello from Lua!')"})
        client.sendall(message.encode('utf-8'))

        # Receive response
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

if __name__ == "__main__":
    main()
