from server import Server
from simulation import Simulation
from steam_manager import SteamManager

import time

def main():
    # Initialize SteamManager
    #steam_manager = SteamManager()

    # Initialize server and simulation
    
    simulation = Simulation(x=3,y=3, map_update_interval=0.5)
    server = Server(simulation)
    try:
        # Start the server
        simulation.start(server.outbound_queue)
        server.start()
        print("Server and simulation running. Press Ctrl+C to stop.")

        # Keep the main thread alive while allowing for interrupt handling
        while server.is_alive() or simulation.running:
            time.sleep(0.5)  # Sleep to avoid busy waiting

    except KeyboardInterrupt:
        print("Shutting down...")

    # Stop both server and simulation
    server.stop()
    simulation.stop()

if __name__ == "__main__":
    main()
