from server import Server
from simulation import simulation_instance
import time

def main():
    # Initialize server and simulation
    server = Server()
    simulation_instance.start(server.outbound_queue)

    try:
        # Start the server
        server.start()
        print("Server and simulation running. Press Ctrl+C to stop.")

        # Keep the main thread alive while allowing for interrupt handling
        while server.is_alive() or simulation_instance.running:
            time.sleep(0.5)  # Sleep to avoid busy waiting

    except KeyboardInterrupt:
        print("Shutting down...")

    # Stop both server and simulation
    server.stop()
    simulation_instance.stop()

if __name__ == "__main__":
    main()
