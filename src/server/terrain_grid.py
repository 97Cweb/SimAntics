class TerrainGrid:
    def __init__(self, lua_runtime, width, height):
        """Initialize the terrain grid."""
        self.lua = lua_runtime
        self.grid = self._create_grid(width, height, {"terrain": 0, "resources": 0})
        self.temp_grid = self._create_grid(width, height, {"terrain": 0, "resources": 0})

    def _create_grid(self, width, height, default):
        return [[self.lua.table_from(default.copy()) for _ in range(width)] for _ in range(height)]

    def update(self, lua_update_func, frame_counter):
        """
        Update the terrain grid using a Lua script.
        """
        self.grid = lua_update_func(self.grid, self.temp_grid, frame_counter)
