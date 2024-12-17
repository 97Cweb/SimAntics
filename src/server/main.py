from server import Server
from simulation import Simulation
from simantics_SteamworksWrapper.steamworks_bindings import steam_lib

import time

def main():
    # Initialize SteamManager
    #steam_manager = SteamManager()

    # Initialize server and simulation
    
    simulation = Simulation(save_name = "test1",x=3,y=3, map_update_interval=0.5, gas_update_interval= 1.0)
    
    # # Load or start fresh
    # load_save = input("Load a save? (y/n): ").strip().lower()
    # if load_save == "yn":
    #    save_name = input("Enter save name: ").strip()
    #    try:
    #        simulation.load(save_name)
    #    except FileNotFoundError as e:
    #        print(e)
    #        return
    
    
    server = Server(simulation)
    simulation.set_server(server)
    
    
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

    # # Save the game before exiting
    # save_game = input("Save the game? (y/n): ").strip().lower()
    # if save_game == "y":
    #     simulation.save()


if __name__ == "__main__":
    main()
