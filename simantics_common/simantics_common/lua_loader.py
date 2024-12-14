import os

def load_lua_scripts(lua_runtime, base_path, mods_path):
    """
    Load Lua scripts from core, replaceable, and mods folders.
    
    Args:
        lua_runtime: LuaRuntime instance.
        base_path: Path to the `lua` folder.
        mods_path: Path to the `mods` folder.
        
    Returns:
        A dictionary mapping script names to their Lua objects.
    """
    
    lua_scripts = {}
    mod_list = []
    #load core and replaceable scripts
    for folder in ["core", "replaceable"]:
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            for file in os.listdir(folder_path):
                name, ext = os.path.splitext(file)
                if ext == ".lua":
                    script_path = os.path.join(folder_path, file)
                    with open(script_path, "r") as f:
                        script_code = f.read()
                        lua_runtime.execute(script_code)
                        lua_scripts[name] = lua_runtime.globals()

    #load mod scripts
    if os.path.exists(mods_path):
        for mod_folder in os.listdir(mods_path):
            mod_list.append(mod_folder)
            mod_path = os.path.join(mods_path, mod_folder)
            if os.path.isdir(mod_path):
                for folder in ["replaceable"]:
                    mod_subfolder = os.path.join(mod_path, folder)
                    if os.path.exists(mod_subfolder):
                        name, ext = os.path.splitext(file)
                        if ext == ".lua":
                            script_path = os.path.join(mod_subfolder, file)
                            with open(script_path, "r") as f:
                                script_code = f.read()
                                lua_runtime.execute(script_code)
                                lua_scripts[name] = lua_runtime.globals()

    return lua_scripts, mod_list