import socket
import json5

HOST = '127.0.0.1'
PORT = 65432

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print("Connected to server.")

        # Send a Lua script command
        lua_script = """
        function test()
            return "Hello from Lua!"
        end

        return test()
        """
        message = json5.dumps({"command": "run_script", "script": lua_script})
        client.sendall(message.encode('utf-8'))

        # Receive response
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

        # Send another command
        command = json5.dumps({"command": "other_action", "details": "Placeholder"})
        client.sendall(command.encode('utf-8'))
        response = client.recv(1024).decode('utf-8')
        print(f"Server response: {response}")

if __name__ == "__main__":
    main()
