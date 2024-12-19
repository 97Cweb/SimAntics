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
        
        self.message_callback = message_callback
        
        
        
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
            self._load_player_scripts()
            
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
        load_scripts_from_folder(self.lua_runtime, setup_scripts_dir, self.lua_scripts, global_reference=True)
        print(f"Core scripts loaded for player: {self.username}")

            
    def _load_core_scripts(self):
        """
        Load the base scripts (`base_ant`, `base_nest`) into the Lua environment.
        """
        core_scripts_dir = "lua/core"
        load_scripts_from_folder(self.lua_runtime, core_scripts_dir, self.lua_scripts, global_reference=True)
        print(f"Core scripts loaded for player: {self.username}")
            
    def _load_player_scripts(self):
        """
        Load player-specific Lua scripts, such as `player_ant` and `player_nest`.
        """
        player_scripts_dir = os.path.join("saves", self.save_name, "players", self.username)
        load_scripts_from_folder(self.lua_runtime, player_scripts_dir, self.lua_scripts, global_reference=True)
        print(f"Player-specific scripts loaded for {self.username}")


    def _load_pheromone_definitions(self):
        """
        Initialize pheromones for this player by loading definitions.
        """
        pheromone_file = os.path.join("saves", self.save_name, "players", self.username, "pheromones.json")
        if os.path.exists(pheromone_file):
            with open(pheromone_file, "r") as f:
                pheromone_definitions = json5.load(f)
                self.pheromone_manager.register_pheromones(self, pheromone_definitions)
                print(f"Pheromones registered for player {self.username}")
        else:
            print(f"No pheromone definition file found for player {self.username}")        

    
    def add_nest(self, nest):
        """
        Add an nest to the player's list of nests.

        Args:
            nest: The nest instance to add.
        """
        self.nests.append(nest)
        print(f"Nest added for player {self.username}. Total nests: {len(self.nests)}")
        
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