import os


def load_lua_scripts(lua_runtime, base_path, mods_path, global_reference = False):
    """
    Load Lua scripts from core, replaceable, and mods folders.
    
    Args:
        lua_runtime: LuaRuntime instance.
        base_path: Path to the `lua` folder.
        mods_path: Path to the `mods` folder.
        
    Returns:
        A tuple:
            - A dictionary mapping script names to their Lua objects.
            - A list of mod names.
    """
    lua_scripts = {}

    # Load core and replaceable scripts
    load_scripts_from_folders(lua_runtime, base_path, ["core", "replaceable"], lua_scripts)

    # Load mod scripts
    mod_list = load_mod_scripts(lua_runtime, mods_path, lua_scripts)

    return lua_scripts, mod_list


def load_scripts_from_folders(lua_runtime, base_path, folders, lua_scripts, global_reference = False):
    """
    Load Lua scripts from specified folders into the lua_scripts dictionary.

    Args:
        lua_runtime: LuaRuntime instance.
        base_path: Path to the base directory containing folders.
        folders: List of folders to search for Lua scripts.
        lua_scripts: Dictionary to store loaded Lua scripts.
    """
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        load_scripts_from_folder(lua_runtime, folder_path, lua_scripts, global_reference)

def load_scripts_from_folder(lua_runtime, folder_path, lua_scripts, global_reference = False):
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            load_lua_script(lua_runtime, folder_path, file, lua_scripts, global_reference)
    

def load_mod_scripts(lua_runtime, mods_path, lua_scripts):
    """
    Load Lua scripts from mods into the lua_scripts dictionary.

    Args:
        lua_runtime: LuaRuntime instance.
        mods_path: Path to the mods directory.
        lua_scripts: Dictionary to store loaded Lua scripts.

    Returns:
        A list of mod folder names.
    """
    mod_list = []
    if os.path.exists(mods_path):
        for mod_folder in os.listdir(mods_path):
            mod_list.append(mod_folder)
            mod_path = os.path.join(mods_path, mod_folder)
            if os.path.isdir(mod_path):
                load_scripts_from_folders(lua_runtime, mod_path, ["replaceable"], lua_scripts)
    return mod_list


def load_lua_script(lua_runtime, folder_path, file, lua_scripts, global_reference = False):
    """
    Load a single Lua script and add it to the lua_scripts dictionary.

    Args:
        lua_runtime: LuaRuntime instance.
        folder_path: Path to the folder containing the Lua script.
        file: Name of the Lua file to load.
        lua_scripts: Dictionary to store the loaded Lua script.
    """
    name, ext = os.path.splitext(file)
    if ext == ".lua":
        script_path = os.path.join(folder_path, file)
        with open(script_path, "r") as f:
            script_code = f.read()
            lua_runtime.execute(script_code)
            if global_reference:
                lua_runtime.globals()[name] = lua_runtime.globals()[name]
            lua_scripts[name] = lua_runtime.globals()
