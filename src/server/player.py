from lupa import LuaRuntime
from lupa.lua54 import LuaError

from simantics_common.lua_loader import load_scripts_from_folder
import os

class Player:
    def __init__(self, username, save_name, is_human=True, ):
        self.username = username
        self.is_human = is_human
        self.client = None  # To track the connected client socket
        self.save_name = save_name
        
        self.lua_runtime = LuaRuntime(unpack_returned_tuples=True)  # Player-specific Lua environment
        self.ants = []  # List of the player's ants
        self.nests = []
        
        self.scripts_loaded = False
        
        self._initialize_lua_environment()
        
    def _initialize_lua_environment(self):
        """
        Set up the Lua environment for the player, including loading core scripts 
        and player-specific extensions.
        """
        try:
                        
            # Load core scripts (base_ant, base_nest)
            self._load_core_scripts()

            # Load player-specific scripts (player_ant, player_nest)
            self._load_player_scripts()

            self.scripts_loaded = True
            print(f"Lua environment initialized for player: {self.username}")
        except Exception as e:
            print(f"Error initializing Lua environment for player {self.username}: {e}")
            self.scripts_loaded = False
            
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
        load_scripts_from_folder(self.lua_runtime, player_scripts_dir, self.lua_scripts, global_reference=False)
        print(f"Player-specific scripts loaded for {self.username}")

    
    def execute_lua_function(self, function_name, *args):
        """
        Execute a Lua function in the player's environment.

        Args:
            function_name (str): The name of the Lua function to execute.
            *args: Arguments to pass to the Lua function.

        Returns:
            The result of the Lua function execution.
        """
        try:
            lua_function = self.lua_runtime.globals().get(function_name)
            if not lua_function:
                raise ValueError(f"Lua function {function_name} not found for player: {self.username}")
            return lua_function(*args)
        except LuaError as e:
            print(f"Lua error in function {function_name} for player {self.username}: {e}")
            return None
        
    def update_scripts(self, script_name, script_code):
        """
        Dynamically update a player's Lua script.

        Args:
            script_name (str): The name of the Lua script being updated (e.g., "player_ant").
            script_code (str): The new Lua script code.
        """
        try:
            self.lua_runtime.execute(script_code)
            print(f"Updated Lua script {script_name} for player: {self.username}")
        except LuaError as e:
            raise RuntimeError(f"Error updating Lua script {script_name} for player {self.username}: {e}")

    def add_ant(self, ant):
        """
        Add an ant to the player's list of ants.

        Args:
            ant: The ant instance to add.
        """
        self.ants.append(ant)
        print(f"Ant added for player {self.username}. Total ants: {len(self.ants)}")