import json

from simulation import simulation_instance

def handle_client(client_socket):
    try:
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            print(f"Received data: {data}")

            # Process the data (e.g., Lua script or commands)
            response = process_client_request(data)

            # Send response back to the client
            client_socket.sendall(response.encode('utf-8'))

    except ConnectionResetError:
        print("Client disconnected abruptly.")
    finally:
        client_socket.close()
        print("Connection closed.")

def process_client_request(data):
    """
    Process client data and return a response.
    This is where Lua scripts or commands will be interpreted.
    """
    # For now, echo the data back
    try:
        request = json.loads(data)
        simulation_instance.command_queue.put(request)
        # Placeholder response
        response = {"status": "success", "message": "Data received"}
    except json.JSONDecodeError:
        response = {"status": "error", "message": "Invalid JSON format"}
    
    return json.dumps(request)
