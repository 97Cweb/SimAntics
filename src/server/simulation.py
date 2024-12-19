import time
import threading
import os
from queue import Queue

from lupa import LuaRuntime

from pheromone_manager import PheromoneManager
from terrain_grid import TerrainGrid
from player import Player
from simulation_saver import SimulationSaver
from simantics_common.lua_loader import LuaLoader



class Simulation:
    def __init__(self, save_name, x=10, y=10, map_update_interval=1.0, gas_update_interval=1.0,max_player_gas_count=32):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.save_name = save_name
        self.server = None
        self.message_callback = None
        
        self.map_update_interval = map_update_interval
        self.gas_update_interval = gas_update_interval
        self.last_map_update = time.time()
        self.last_gas_update = time.time()
        
        self.frame_counter = 0
        self.running = False
        
        self.command_queue = Queue()
        self.players = {}
        
        self.terrain_grid = TerrainGrid(self.lua, x, y)
        self.pheromone_manager = PheromoneManager(self.lua, x, y, max_player_gas_count=max_player_gas_count)

        # Load core and mod Lua scripts
        base_path = "lua"
        mods_path = "mods"
        core_scripts = LuaLoader.load_scripts_from_folder(self.lua, os.path.join(base_path, "core"))
        replaceable_scripts = LuaLoader.load_scripts_from_folder(self.lua, os.path.join(base_path, "replaceable"))
        mod_scripts = LuaLoader.load_scripts_from_folder(self.lua, mods_path)

        # Merge core, replaceable, and mod scripts
        self.lua_scripts = {**core_scripts, **replaceable_scripts, **mod_scripts}
        print("Loaded Lua scripts:", self.lua_scripts)

        
        
        self._initialize_lua_functions()

    def _initialize_lua_functions(self):
        try:
            self.map_update_func = self.lua_scripts.get("map_update")
            self.gas_update_func = self.lua_scripts.get("gas_update")
            if not self.map_update_func or not self.gas_update_func:
                raise RuntimeError("Update scripts not found.")
        except Exception as e:
            raise RuntimeError(f"Error initializing Lua functions: {e}")

    def start(self, server_outbound_queue):
        SimulationSaver.save_simulation(self, self.save_name)
        self.running = True
        self.server_outbound_queue = server_outbound_queue
        threading.Thread(target=self.run, daemon=True).start()

    def stop(self):
        self.running = False

    def run(self):
        print("Simulation started.")
        while self.running:
            self.update()
            time.sleep(0.1)

    def update(self):
        self.frame_counter += 1
        current_time = time.time()
        while not self.command_queue.empty():
          command = self.command_queue.get()
          print(f"Processing command: {command}")
          self.process_command(command)
        

        state_updated = False
        if current_time - self.last_map_update >= self.map_update_interval:
            self.last_map_update = current_time
            self.terrain_grid.update(self.map_update_func, self.frame_counter)
            state_updated = True

        if current_time - self.last_gas_update >= self.gas_update_interval:
            self.last_gas_update = current_time
            self.pheromone_manager.update(self.gas_update_func,self.frame_counter)
            state_updated = True

        if state_updated:
            self.broadcast_update({"frame": self.frame_counter, "map": self.terrain_grid, "gas": self.pheromone_manager})


        for player in self.players.values():
            player.update()
        

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
                    self.create_player(username)
        else:
            print(f"Unhandled command: {command}")

    # New player-related methods
    def create_player(self, username):
        """Create a new player in the simulation and generate their folder and Lua scripts."""
        if username in self.players:
            print(f"Player {username} already exists.")
            return

        else:
            print("here")
            # Create player folder
            SimulationSaver.create_player_folder(self.save_name,username)
        
        # Add player to simulation
        self.players[username] = Player(username, self.save_name, self.pheromone_manager, message_callback=self.message_callback)
        print(f"Player {username} added to the simulation.")


    def broadcast_update(self, state):
        self.server_outbound_queue.put(state)
        
    def set_server(self, server):
        self.server = server
        self.message_callback = self.server.message_throttler.add_message
        
