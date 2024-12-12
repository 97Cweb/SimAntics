from server import Server
from simulation import Simulation
from steamworks_wrapper import steamworks_bindings
from ctypes import c_void_p, c_int
import time

def main():
    # Initialize Steamworks API
    if not steamworks_bindings.steam_lib.SteamAPI_InitFlat():
        raise RuntimeError("Steamworks API initialization failed")
        
    print(steamworks_bindings.steam_lib)
    # Obtain the ISteamClient instance
    #steamworks_bindings.steam_lib.SteamAPI_SteamClient.argtypes = []
    #steamworks_bindings.steam_lib.SteamAPI_SteamClient.restype = c_void_p
    #steam_client = steamworks_bindings.steam_lib.SteamAPI_SteamClient()
    #if not steam_client:
    #    raise RuntimeError("Failed to obtain ISteamClient instance")

    # Create the Steam pipe
    #steamworks_bindings.steam_lib.SteamAPI_ISteamClient_CreateSteamPipe.argtypes = [c_void_p]
    #steamworks_bindings.steam_lib.SteamAPI_ISteamClient_CreateSteamPipe.restype = c_int
    #steam_pipe = steamworks_bindings.steam_lib.SteamAPI_ISteamClient_CreateSteamPipe(steam_client)
    #if steam_pipe == 0:
    #    raise RuntimeError("Failed to create Steam pipe")
    #print(f"Steam Pipe: {steam_pipe}")
    
    
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
