import os
from lupa.lua54 import LuaError

class LuaLoader:
    @staticmethod
    def load_scripts_from_folder(lua_runtime, folder_path):
        """
        Load all Lua scripts from a given folder into the Lua runtime.

        Args:
            lua_runtime: LuaRuntime instance.
            folder_path: Path to the folder containing Lua scripts.

        Returns:
            A dictionary mapping script names to their functions/tables or None if missing.
        """
        lua_scripts = {}
        if not os.path.exists(folder_path):
            print(f"Warning: Folder '{folder_path}' does not exist.")
            return lua_scripts

        for file in os.listdir(folder_path):
            name, ext = os.path.splitext(file)
            if ext == ".lua":
                script_path = os.path.join(folder_path, file)
                print(f"Processing script: {script_path}")
                with open(script_path, "r") as f:
                    script_code = f.read()
                    try:
                        # Execute the Lua script
                        lua_script = lua_runtime.execute(script_code)
                        
                        # First, try capturing returned value
                        if lua_script:
                            lua_scripts[name] = lua_script
                            print(f"Successfully loaded '{name}' from script return.")
                        # If no return value, check globals
                        elif name in lua_runtime.globals():
                            lua_scripts[name] = lua_runtime.globals()[name]
                            print(f"Successfully loaded '{name}' from globals.")
                        else:
                            lua_scripts[name] = None
                            print(f"Warning: Script '{name}' did not define or return a valid function/table.")
                    except LuaError as e:
                        print(f"Error loading script '{name}': {e}")
                        lua_scripts[name] = None
        return lua_scripts

    @staticmethod
    def load_core_scripts(lua_runtime, base_path):
        """
        Load core scripts (e.g., from 'lua/core' or 'lua/replaceable').

        Args:
            lua_runtime: LuaRuntime instance.
            base_path: Path to the 'lua' folder.

        Returns:
            A dictionary of Lua script names mapped to their functions or None if missing.
        """
        core_folders = ["core", "replaceable"]
        core_scripts = {}
        for folder in core_folders:
            folder_path = os.path.join(base_path, folder)
            scripts = LuaLoader.load_scripts_from_folder(lua_runtime, folder_path)
            core_scripts.update(scripts)
        return core_scripts

    @staticmethod
    def load_mod_scripts(lua_runtime, mods_path):
        """
        Load mod scripts from the 'mods' folder.

        Args:
            lua_runtime: LuaRuntime instance.
            mods_path: Path to the 'mods' folder.

        Returns:
            A dictionary of Lua script names mapped to their functions or None if missing.
        """
        return LuaLoader.load_scripts_from_folder(lua_runtime, mods_path)
