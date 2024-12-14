import time
import threading

from player import Player

from lupa import LuaRuntime
from queue import Queue

class Simulation:
    def __init__(self, x=10, y=10, map_update_interval=1.0):
        
        self.lua = LuaRuntime(unpack_returned_tuples=True)  # Initialize Lua runtime
        
        self.grid = [[self.lua.table_from({"terrain": 0, "resources": 0}) for _ in range(x)] for _ in range(y)]
        self.temp_grid = [[self.lua.table_from({"terrain": 0, "resources": 0}) for _ in range(x)] for _ in range(y)]
        self.x = x
        self.y = y
        
        self.map_update_interval = map_update_interval
        self.game_state = {"nests": [], "ants": [], "resources": []}
        self.running = False
        self.command_queue = Queue()
        self.players = {}
        self.frame_counter = 0   
        
        self.last_map_update = time.time()
        
        
        try:
            with open("lua/replaceable/map_update_script.lua", "r") as f:
                map_update_code = f.read()
            self.lua.execute(map_update_code)
            self.map_update_func = self.lua.globals().map_update
        except FileNotFoundError:
            raise RuntimeError("Map update script not found in replaceable folder.")
    
        

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
        current_time = time.time()
        while not self.command_queue.empty():
           
           command = self.command_queue.get()
           print(f"Processing command: {command}")
           self.process_command(command)
        
        
        # Update map
        if current_time - self.last_map_update >= self.map_update_interval:
            self.last_map_update = current_time
            self.update_map()
            
            state = {
                "frame": self.frame_counter,
                "map": self.grid
            }
            
            self.broadcast_update(state)
        
        self.frame_counter += 1

        """Run one tick of the game simulation."""
        print("Simulating one game tick...")


    def broadcast_update(self, state):
        self.server_outbound_queue.put(state)
        
        
    def update_map(self):
        """Update the grid state for growth using the Lua script."""
        #print(self.format_grid())
        
        # Run the Lua script
        self.grid = self.map_update_func(self.grid, self.temp_grid, self.frame_counter)
        

    def format_grid(self):
        """Convert the grid to a human-readable format for printing."""
        formatted_grid = []
        for row in self.grid:
            formatted_row = []
            for cell in row:
                # Extract data from the Lua table
                formatted_row.append({
                    "terrain": cell["terrain"],
                    "resources": cell["resources"]
                })
            formatted_grid.append(formatted_row)
        return formatted_grid


    def set_map_update_script(self, lua_script):
        """Set a custom Lua script for growth updates."""
        self.map_update_script = self.lua.eval(lua_script)
        
        
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
            