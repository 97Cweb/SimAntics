class TerrainGrid:
    def __init__(self, lua_runtime, grid=None, width=None, height=None):
        """Initialize the terrain grid."""
        self.lua = lua_runtime
        if grid:
            self.grid = self._load_grid(grid)
        elif width is not None and height is not None:
            self.grid = self._create_grid(width, height, {"terrain": 0, "resources": 0})
        else:
            raise ValueError("Either grid or dimensions (width, height) must be provided.")

        self.temp_grid = self._create_grid(len(self.grid[0]), len(self.grid), {"terrain": 0, "resources": 0})

    def _create_grid(self, width, height, default):
        return [[self.lua.table_from(default.copy()) for _ in range(width)] for _ in range(height)]

    def _load_grid(self, grid_data):
        return [[self.lua.table_from(cell) for cell in row] for row in grid_data]

    def update(self, lua_update_func, frame_counter):
        """Update the terrain grid using a Lua script."""
        self.grid = lua_update_func(self.grid, self.temp_grid, frame_counter)
