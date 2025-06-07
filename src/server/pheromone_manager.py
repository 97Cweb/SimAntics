import uuid
from collections import defaultdict

class PheromoneManager:
    def __init__(self,lua_runtime, width = None, height = None, max_player_gas_count=32, grid=None, pheromone_definitions=None, uuid_to_pheromone=None ):
        """
       Initialize the pheromone manager.

       Args:
           lua_runtime: Lua runtime instance for executing Lua scripts.
           width (int): Optional width of the grid (ignored if grid is provided).
           height (int): Optional height of the grid (ignored if grid is provided).
           max_player_gas_count (int): Maximum number of pheromones a player can have.
           grid (dict): Preloaded pheromone grid data (optional).
           pheromone_definitions (dict): Preloaded pheromone definitions (optional).
           uuid_to_pheromone (dict): Preloaded UUID mappings (optional).
       """
        self.lua_runtime = lua_runtime
        self.max_player_gas_count = max_player_gas_count

        # Handle grid initialization
        if grid and grid.keys():
            self.grid = grid
            # Infer dimensions from the first pheromone layer
            first_layer = next(iter(grid.values()))
            self.height = len(first_layer)
            self.width = len(first_layer[0]) if self.height > 0 else 0
        else:
            # Use provided dimensions or default to empty
            self.width = width or 0
            self.height = height or 0
            self.grid = defaultdict(lambda: [[0.0 for _ in range(self.width)] for _ in range(self.height)])



        # Mapping for player anonymity
        # Definitions: player_id -> [{pheromone_name, uuid, decay, diffusion}]
        self.pheromone_definitions = pheromone_definitions or defaultdict(list)

        # Reverse mapping for UUID lookup
        self.uuid_to_pheromone = uuid_to_pheromone  or {}  # UUID -> (player_id, pheromone_name)
        
        
    def register_pheromones(self, player, definitions):
        """
        Register multiple pheromones for a player.

        Args:
            player (Player): Player
            definitions (list): List of pheromone definitions (dicts with name, decay, diffusion).
        """
        player_id = player.username
        
        num_definitions = len(definitions)
        num_existing_pheromones = len(self.pheromone_definitions[player_id])
        if num_definitions + num_existing_pheromones > self.max_player_gas_count:
            player.print(f"Player {player_id} trying to add too many pheromones. Existing {num_existing_pheromones} + new {num_definitions} is greater than {self.max_player_gas_count}")
            
        for definition in definitions:
            name = definition.get("name")
            decay = definition.get("decay", 0.1)
            diffusion = definition.get("diffusion", 0.25)
            col = definition.get("col", "#000000")

            # Avoid duplicates
            if any(p['name'] == name for p in self.pheromone_definitions[player_id]):
                continue

            # Generate a UUID for this pheromone
            pheromone_uuid = str(uuid.uuid4())
            definition["uuid"] = pheromone_uuid
            self.pheromone_definitions[player_id].append({
                "name": name,
                "uuid": pheromone_uuid,
                "decay": decay,
                "diffusion": diffusion,
                "col": col
            })

            # Update reverse mapping
            self.uuid_to_pheromone[pheromone_uuid] = (player_id, name)


    def get_pheromone_uuid(self, player_id, pheromone_name):
        """
        Retrieve the UUID for a player's pheromone by name.
        """
        for pheromone in self.pheromone_definitions[player_id]:
            if pheromone["name"] == pheromone_name:
                return pheromone["uuid"]
        return None
    
    def emit_pheromone(self, x, y, pheromone_uuid, amount):
        """
        Emit a pheromone at a specific grid location.

        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.
            pheromone_uuid (str): The UUID of the pheromone being emitted.
            amount (float): The amount of pheromone to emit.
        """
        if 0 <= y < self.height and 0 <= x < self.width:
            if pheromone_uuid not in self.grid:
                self.grid[pheromone_uuid] = [[0.0 for _ in range(self.width)] for _ in range(self.height)]
            self.grid[pheromone_uuid][y][x] += amount

    def smell_pheromones(self, x, y, radius, player_id):
        """
        Smell pheromones in a radius around (x, y).
        
        Args:
            x (int): X-coordinate.
            y (int): Y-coordinate.
            radius (int): Radius for smelling pheromones.
            player_id (str): ID of the player calling this method.

        Returns:
            dict: Smelled pheromone amounts.
        """
        smelled = defaultdict(float)

        for pheromone_uuid, layer in self.grid.items():
            for dy in range(-radius, radius + 1):
                for dx in range(-radius, radius + 1):
                    nx, ny = x + dx, y + dy
                    if 0 <= ny < self.height and 0 <= nx < self.width:
                        if pheromone_uuid in self.uuid_to_pheromone:
                            owner_id, pheromone_name = self.uuid_to_pheromone[pheromone_uuid]
                            if owner_id == player_id:
                                smelled[pheromone_name] += layer[ny][nx]
                            else:
                                smelled[pheromone_uuid] += layer[ny][nx]
        return dict(smelled)

    def update(self, lua_func, frame):
        """
        Update the pheromone grid using a Lua function.

        Args:
            lua_func: A Lua function to update the pheromone grid.
            frame (int): The current simulation frame.
        """
        try:

            # Wrap the grid as a Lua-compatible table for the Lua function
            lua_grid = self._grid_to_lua()
            temp_grid = self._create_empty_lua_grid()

            # Execute the Lua update function
            lua_func(lua_grid, temp_grid, frame)

            # Convert the updated Lua grid back into Python format
            self._lua_to_grid(temp_grid)
        except Exception as e:
            print(f"[Error] Failed to update pheromone grid: {e}")

    def _grid_to_lua(self):
        """Convert the grid to a Lua-compatible format."""
        lua_grid = self.lua_runtime.table()
        for pheromone_uuid, layer in self.grid.items():
            lua_layer = self.lua_runtime.table()
            for y, row in enumerate(layer):
                lua_row = self.lua_runtime.table()
                for x, value in enumerate(row):
                    lua_row[x + 1] = value  # Lua uses 1-based indexing
                lua_layer[y + 1] = lua_row
            lua_grid[pheromone_uuid] = lua_layer
        return lua_grid


    def _lua_to_grid(self, lua_grid):
        """Convert Lua table back into Python grid format."""
        for pheromone_uuid, lua_layer in lua_grid.items():
            self.grid[pheromone_uuid] = [
                [lua_layer[y + 1][x + 1] for x in range(self.width)] for y in range(self.height)
            ]

    def _create_empty_lua_grid(self):
        """Create an empty Lua-compatible grid structure."""
        lua_grid = self.lua_runtime.table()
        for pheromone_uuid in self.grid.keys():  # Loop over pheromone IDs
            lua_layer = self.lua_runtime.table()
            for y in range(self.height):
                lua_row = self.lua_runtime.table()
                for x in range(self.width):
                    lua_row[x + 1] = 0.0  # Initialize cells with 0.0
                lua_layer[y + 1] = lua_row
            lua_grid[pheromone_uuid] = lua_layer
        return lua_grid
