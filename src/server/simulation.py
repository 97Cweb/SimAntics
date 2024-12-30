import time
import threading
import os
import logging
from queue import Queue

from lupa import LuaRuntime

from pheromone_manager import PheromoneManager
from terrain_grid import TerrainGrid
from player import Player
from simulation_saver import SimulationSaver
from simantics_common.lua_loader import LuaLoader


# Configure logging
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG for more detailed logs
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

if not logger.hasHandlers():
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    logger.addHandler(console_handler)
    logger.info("Default console logging is active.")



class Simulation:
    def __init__(self, save_name, x=10, y=10, map_update_interval=1.0, gas_update_interval=1.0, max_player_gas_count=32, mod_list = []):
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.save_name = save_name
        self.server = None
        self.message_callback = None

        self.active_mods = []  # Dictionary to track enabled mods

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
        
        # Initialize Lua scripts
        self.lua_scripts = {}

        # Load core and replaceable Lua scripts
        base_path = "lua"
        core_scripts = LuaLoader.load_scripts_from_folder(self.lua, os.path.join(base_path, "core"))
        replaceable_scripts = LuaLoader.load_scripts_from_folder(self.lua, os.path.join(base_path, "replaceable"))

        self._process_mods(mod_list)

        # Merge scripts, giving priority to mods
        self.lua_scripts.update(core_scripts)
        self.lua_scripts.update(replaceable_scripts)
        logger.info("Loaded Lua scripts: %s", self.lua_scripts)

        

        # Initialize Lua functions
        self._initialize_lua_functions()

    def _process_mods(self, mod_list):
        """
        Process the given list of mods in order and load them.
    
        Args:
            mod_list (list): A list of dictionaries containing mod information, including:
                             - name: The name of the mod.
                             - enabled: Whether the mod is enabled.
                             - load_order: The mod's load order.
        """
        mod_replaceable_scripts = {}
        mod_players_scripts = {}
    
        mods_path = "mods"
    
        for mod in mod_list:    
            mod_path = os.path.join(mods_path, mod)
            print(mod_path)
            if os.path.isdir(mod_path):
                self.active_mods.append(mod)
            else:
                logger.warning("Mod '%s' is missing or not a directory.", mod)
                continue
        
    
            # Load replaceable scripts
            replaceable_path = os.path.join(mod_path, "replaceable")
            if os.path.isdir(replaceable_path):
                replaceable_scripts = LuaLoader.load_scripts_from_folder(self.lua, replaceable_path)
                mod_replaceable_scripts.update(replaceable_scripts)
    
            # Load player scripts
            players_path = os.path.join(mod_path, "players")
            if os.path.isdir(players_path):
                for player_name in os.listdir(players_path):
                    player_path = os.path.join(players_path, player_name)
                    if os.path.isdir(player_path):
                        player_script = LuaLoader.load_scripts_from_folder(self.lua, player_path)
                        mod_players_scripts[player_name] = player_script
    
        print(self.active_mods)
        # Merge mod scripts with core and replaceable scripts
        self.lua_scripts.update(mod_replaceable_scripts)
        self._initialize_ai_players(mod_players_scripts)


    def _initialize_ai_players(self, mod_players_scripts):
        for player_name, script in mod_players_scripts.items():
            if script is None:
                logger.warning("Player '%s' failed to load.", player_name)
                continue
            logger.info("Creating AI player '%s'.", player_name)
            self.create_player(player_name, is_human=False)

    def _initialize_lua_functions(self):
        try:
            self.map_update_func = self.lua_scripts.get("map_update")
            self.gas_update_func = self.lua_scripts.get("gas_update")
            if not self.map_update_func or not self.gas_update_func:
                raise RuntimeError("Update scripts not found.")
        except Exception as e:
            logger.error("Error initializing Lua functions: %s", e)
            raise

    def start(self, server_outbound_queue):
        SimulationSaver.save_simulation(self, self.save_name)
        self.running = True
        self.server_outbound_queue = server_outbound_queue
        threading.Thread(target=self.run, daemon=True).start()

    def stop(self):
        self.running = False

    def run(self):
        logger.info("Simulation started.")
        while self.running:
            self.update()
            time.sleep(0.1)

    def update(self):
        self.frame_counter += 1
        current_time = time.time()
        while not self.command_queue.empty():
            command = self.command_queue.get()
            logger.info("Processing command: %s", command)
            self.process_command(command)

        state_updated = False
        if current_time - self.last_map_update >= self.map_update_interval:
            self.last_map_update = current_time
            self.terrain_grid.update(self.map_update_func, self.frame_counter)
            state_updated = True

        if current_time - self.last_gas_update >= self.gas_update_interval:
            self.last_gas_update = current_time
            self.pheromone_manager.update(self.gas_update_func, self.frame_counter)
            state_updated = True

        if state_updated:
            self.broadcast_update({"frame": self.frame_counter, "map": self.terrain_grid, "gas": self.pheromone_manager})

        for player in self.players.values():
            player.update()

    def process_command(self, command):
        if "event" in command:
            if command["event"] == "login":
                username = command["username"]
                if username not in self.players:
                    logger.info("Adding player '%s'.", username)
                    self.create_player(username)
        else:
            logger.warning("Unhandled command: %s", command)

    def create_player(self, username, is_human=True):
        if username in self.players:
            logger.info("Player '%s' already exists.", username)
            return

        elif is_human:
            SimulationSaver.create_player_folder(self.save_name, username)

        self.players[username] = Player(username, self.save_name, self.pheromone_manager, message_callback=self.message_callback, is_human=is_human)
        logger.info("Player '%s' added to the simulation.", username)

    def broadcast_update(self, state):
        self.server_outbound_queue.put(state)

    def set_server(self, server):
        self.server = server
        self.message_callback = self.server.message_throttler.add_message

    def add_log_handler(self,handler):
        """
        Attach a log handler dynamically.
    
        Args:
            handler: A logging.Handler instance to attach.
        """
        logger.addHandler(handler)
        logger.info("A new log handler has been attached.")