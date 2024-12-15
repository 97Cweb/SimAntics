import time
import threading
from queue import Queue
from player import Player
from simulation_saver import SimulationSaver
from lua_handlers import LuaHandlers
from lupa import LuaRuntime


class Simulation:
    def __init__(self, save_name, x=10, y=10, map_update_interval=1.0, gas_update_interval=1.0):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.grid = self._create_grid(x, y, {"terrain": 0, "resources": 0})
        self.temp_grid = self._create_grid(x, y, {"terrain": 0, "resources": 0})
        self.gas_grid = self._create_grid(x, y, {})
        self.temp_gas_grid = self._create_grid(x, y, {})
        self.save_name = save_name
        self.map_update_interval = map_update_interval
        self.gas_update_interval = gas_update_interval
        self.game_state = {"nests": [], "ants": [], "resources": []}
        self.running = False
        self.command_queue = Queue()
        self.players = {}
        self.frame_counter = 0
        self.last_map_update = time.time()
        self.last_gas_update = time.time()

        # Load Lua scripts
        base_path, mods_path = "lua", "mods"
        self.lua_scripts, self.mod_list = LuaHandlers.load_lua_scripts(self.lua, base_path, mods_path)
        print(self.lua_scripts)
        self._initialize_lua_functions()

    def _create_grid(self, x, y, default):
        return [[self.lua.table_from(default.copy()) for _ in range(x)] for _ in range(y)]

    def _initialize_lua_functions(self):
        if "map_init" in self.lua_scripts:
            self.grid = LuaHandlers.execute_lua_function(self.lua_scripts["map_init"].map_init, self.grid, self.temp_grid, self.frame_counter)
        else:
            raise RuntimeError("Map init script not found.")
        self.map_update_func = self.lua_scripts["map_update"].map_update
        self.gas_update_func = self.lua_scripts["gas_update"].gas_update
        if not self.map_update_func or not self.gas_update_func:
            raise RuntimeError("Update scripts not found.")

    def save(self):
        SimulationSaver.save(self.save_name, self.frame_counter, self.mod_list, self.grid, self.gas_grid, self.players)

    def load(self):
        self.frame_counter, self.grid, self.gas_grid, self.players = SimulationSaver.load(self.lua, self.save_name)

    def start(self, server_outbound_queue):
        self.save()
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
        
        current_time = time.time()
        while not self.command_queue.empty():
          command = self.command_queue.get()
          print(f"Processing command: {command}")
          self.process_command(command)
        

        state_updated = False
        if current_time - self.last_map_update >= self.map_update_interval:
            self.last_map_update = current_time
            self.update_map()
            state_updated = True

        if current_time - self.last_gas_update >= self.gas_update_interval:
            self.last_gas_update = current_time
            self.update_gas()
            state_updated = True

        if state_updated:
            self.broadcast_update({"frame": self.frame_counter, "map": self.grid, "gas": self.gas_grid})

        self.frame_counter += 1

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

        # Create player folder
        SimulationSaver.create_player_folder(self.save_name,username)
        
        # Add player to simulation
        self.players[username] = Player(username, self.save_name)
        print(f"Player {username} added to the simulation.")

        

    

    def broadcast_update(self, state):
        self.server_outbound_queue.put(state)

    def update_map(self):
        self.grid = LuaHandlers.execute_lua_function(self.map_update_func, self.grid, self.temp_grid, self.frame_counter)

    def update_gas(self):
        self.gas_grid = LuaHandlers.execute_lua_function(self.gas_update_func, self.gas_grid, self.temp_gas_grid, self.frame_counter)
