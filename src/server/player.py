import json5
import os
from lupa import LuaRuntime
from lupa.lua54 import LuaError

from simantics_common.lua_loader import LuaLoader
from nest import Nest

class Player:
    def __init__(self, username, save_name, pheromone_manager,  is_human=True, message_callback = None):
        self.username = username
        self.is_human = is_human
        self.client = None  # To track the connected client socket
        self.save_name = save_name
                
        self.lua_runtime = LuaRuntime(unpack_returned_tuples=True)  # Player-specific Lua environment
        self.nests = []
        self.pheromone_manager = pheromone_manager
        
        self.scripts_loaded = False
        self.lua_scripts = {}  # Dictionary for loaded scripts
        
        # Default message callback to a simple logger if not provided
        self.message_callback = message_callback or self._default_message_logger
        
        
        
        self._initialize_lua_environment()
        
        
        
        self.add_nest(Nest(self, self.pheromone_manager))
        
    def update(self):
        self._update_nests()
    
    
    
    def _update_nests(self):
        for nest in self.nests:
            nest.update(self.lua_runtime)
        
    def _initialize_lua_environment(self):
        """
        Set up the Lua environment for the player, including loading core scripts 
        and player-specific extensions.
        """
        try:
            
            # Load the sandbox environment
            self._load_setup_scripts()
                        
            # Load core scripts (base_ant, base_nest)
            self._load_core_scripts()

            # Load player-specific scripts (player_ant, player_nest)
            
            if self.is_human:
                self._load_human_player_scripts()
            else:
                self._load_ai_player_scripts()
            
            self._redirect_lua_print()

            self.scripts_loaded = True
            print(f"Lua environment initialized for player: {self.username}")
        except Exception as e:
            print(f"Error initializing Lua environment for player {self.username}: {e}")
            self.scripts_loaded = False
            
        try:
            # Load pheromone definitions from JSON5
            self._load_pheromone_definitions()
            print(f"Pheromones loaded for player: {self.username}")
        except Exception as e:
            print(f"[Error] Failed to load pheromones for player {self.username}: {e}")

            
   
    def _load_setup_scripts(self):
        """
        Load foundational Lua scripts required for setting up the Lua environment.
        These scripts reside in the 'lua/setup' folder.
        """
        setup_scripts_dir = "lua/setup"
        self.lua_scripts.update(LuaLoader.load_scripts_from_folder(self.lua_runtime, setup_scripts_dir))
        print(f"Core scripts loaded for player: {self.username}")

            
    def _load_core_scripts(self):
        """
        Load the base scripts (`base_ant`, `base_nest`) into the Lua environment.
        """
        core_scripts_dir = "lua/core"
        self.lua_scripts.update(LuaLoader.load_scripts_from_folder(self.lua_runtime, core_scripts_dir))
        print(f"Core scripts loaded for player: {self.username}")
            
    def _load_human_player_scripts(self):
        """
        Load player-specific Lua scripts, such as `player_ant` and `player_nest`.
        """
        player_scripts_dir = os.path.join("saves", self.save_name, "players", self.username)
        self.lua_scripts.update(LuaLoader.load_scripts_from_folder(self.lua_runtime, player_scripts_dir))
        print(f"Player-specific scripts loaded for {self.username}")

    def _load_ai_player_scripts(self):
        """
        Load scripts for AI players from the mods directory.
        """
        player_scripts_dir = self._find_mod_player_path(self.username)
    
        if not player_scripts_dir:
            print(f"Error: AI player scripts for '{self.username}' not found in mods.")
            return
    
        # Load scripts for the AI player
        self.lua_scripts.update(LuaLoader.load_scripts_from_folder(self.lua_runtime, player_scripts_dir))
        print(f"AI player scripts loaded for {self.username} from {player_scripts_dir}")
        
    def _load_pheromone_definitions(self):
        """
        Initialize pheromones for this player by loading definitions.
        For human players, load from the saves directory.
        For AI players, load from the mods directory.
        """
        if self.is_human:
            # Path for human players
            pheromone_file = os.path.join("saves", self.save_name, "players", self.username, "pheromones.json")
        else:
            # Path for AI players
            player_scripts_dir = self._find_mod_player_path(self.username)
            pheromone_file = os.path.join(player_scripts_dir, "pheromones.json") if player_scripts_dir else None
    
        if pheromone_file and os.path.exists(pheromone_file):
            try:
                with open(pheromone_file, "r") as f:
                    pheromone_definitions = json5.load(f)
                    self.pheromone_manager.register_pheromones(self, pheromone_definitions)
                    print(f"Pheromones registered for player {self.username}")
            except Exception as e:
                print(f"[Error] Failed to load pheromone definitions for {self.username}: {e}")
        else:
            print(f"No pheromone definition file found for player {self.username}")

    def _find_mod_player_path(self, player_name):
        """
        Locate the path to a player's folder inside the mods directory.
    
        Args:
            player_name: The name of the player to locate.
    
        Returns:
            The path to the player's folder if found, or None otherwise.
        """
        mods_path = "mods"
        for mod_name in os.listdir(mods_path):
            mod_path = os.path.join(mods_path, mod_name)
            players_path = os.path.join(mod_path, "players")
            if os.path.isdir(players_path):
                player_path = os.path.join(players_path, player_name)
                if os.path.isdir(player_path):
                    return player_path
        return None
    


    def add_nest(self, nest):
        """
        Add an nest to the player's list of nests.

        Args:
            nest: The nest instance to add.
        """
        self.nests.append(nest)
        print(f"Nest added for player {self.username}. Total nests: {len(self.nests)}")
        
        
    def _default_message_logger(self, username, message):
        print(f"[{username}]: {message}")
        
    def _redirect_lua_print(self):
        """
        Redirect the Lua `print` function to a custom Python function.
        """
        self.lua_runtime.globals()["print"] = self._lua_print
        
    def _lua_print(self, *args):
        """
        Custom print function for Lua that redirects output to the callback.
        """
        message = " ".join(map(str, args))
        self.message_callback(self.username, f"[Lua]: {message}")

    def print(self, message):
        """
        Custom print method for Python components.
        """
        self.message_callback(self.username, f"[Python]: {message}")