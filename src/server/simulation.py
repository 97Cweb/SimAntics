import time
import threading

from player import Player

from lupa import LuaRuntime
from queue import Queue

class Simulation:
    def __init__(self):
        self.game_state = {"nests": [], "ants": [], "resources": []}
        self.running = False
        self.command_queue = Queue()
        self.lua = LuaRuntime(unpack_returned_tuples=True)  # Initialize Lua runtime
        self.players = {}
        self.frame_counter = 0
        

    def start(self,server_outbound_queue):
        """Start the simulation loop in a separate thread."""
        self.running = True
        self.server_outbound_queue = server_outbound_queue
        simulation_thread = threading.Thread(target=self.run, daemon=True)
        simulation_thread.start()

    def stop(self):
        """Stop the simulation."""
        self.running = False

    def run(self):
        """Run the simulation loop."""
        print("Simulation started.")
        while self.running:
            self.update()
            time.sleep(0.1)  # Adjust the tick rate (e.g., 10 ticks per second)

    def update(self):
        
        while not self.command_queue.empty():
           command = self.command_queue.get()
           print(f"Processing command: {command}")
           self.process_command(command)
           
        self.frame_counter += 1
        
        state = {
            "frame": self.frame_counter,
            "players": {username: {"human": player.is_human} for username, player in self.players.items()}
        }
        self.server_outbound_queue.put(state)
           
        """Run one tick of the game simulation."""
        print("Simulating one game tick...")

    def process_command(self, command):
        """
        Handle commands from the queue.
        Commands can include Lua scripts or other client actions.
        """
        if "event" in command:
            if command["event"] == "login":
                username = command["username"]
                if username not in self.players:
                    print("adding player")
                    self.players[username] = Player(username)
        else:
            print(f"Unhandled command: {command}")
    
    def execute_lua(self, script):
        """Execute a Lua script."""
        try:
            result = self.lua.execute(script)
            print(f"Lua script executed successfully: {result}")
        except Exception as e:
            print(f"Error executing Lua script: {e}")
            
            
# Singleton simulation instance
simulation_instance = Simulation()
