from lupa.lua54 import LuaError


class LuaHandlers:
    @staticmethod
    def load_lua_scripts(lua_runtime, base_path, mods_path):
        from simantics_common.lua_loader import load_lua_scripts
        return load_lua_scripts(lua_runtime, base_path, mods_path)

    @staticmethod
    def execute_lua_function(func, *args):
        try:
            return func(*args)
        except LuaError as e:
            print(f"Lua error: {e}")
            return None
