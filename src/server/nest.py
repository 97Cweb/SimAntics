from memory import Memory
from ant import Ant
class Nest:
    def __init__(self, player, pheromone_manager, memory_size = 128, x = 0, y=0, spawn_callback=None):
        self.x = x
        self.y = y
        self.player = player
        self.pheromone_manager = pheromone_manager
        self.memory = Memory(max_len=memory_size, default_value=None, shift_callback=self._on_memory_shift)
        self.ants = []
        
        self.spawn_ant()
    
    def smell(self):
        """Simulate nest smelling."""
        self.player.print("nest {self.nest_id} is smelling surroundings")
        return []

    def spawn_ant(self):
        """Spawn a new Ant and notify the simulation."""
        new_ant = Ant(player= self.player, pheromone_manager= self.pheromone_manager, x=self.x, y = self.y)
        self.ants.append(new_ant)
            
    def emit_pheromone(self, pheromone_name, amount):
        pheromone_uuid = self.pheromone_manager.get_pheromone_uuid(self.player.username, pheromone_name)
        if pheromone_uuid:
            self.pheromone_manager.emit_pheromone(self.x, self.y, pheromone_uuid, amount)
        else:
            self.player.print(f"[Warning] Pheromone '{pheromone_name}' not registered for player {self.player.username}.")
    
       
    def update(self, lua_runtime):
        """Update nest behavior using the Lua script."""
        
        try:
            # Create Lua runtime globals and expose Python methods
            lua_globals  = lua_runtime.globals()
            
            base_nest_table = lua_globals.Base_Nest
            if base_nest_table is None:
                raise ValueError("Base_Nest not found in Lua globals.")
                
            # Set specific Python functions as attributes of Base_Nest
            base_nest_table.smell = self.smell
            base_nest_table.spawn_ant = self.spawn_ant
    
            # Provide controlled access to memory (read/write, no expansion)
            base_nest_table.memory = {
           "get": self.memory.getitem,
           "set": self.memory.setitem,
           "add": self.memory.add,
           "shift": self.memory.shift,
           
       }
    
            
            # Call the Lua script's "update" function
            lua_update = base_nest_table.update  # Don't call it yet (no parentheses)
            if lua_update:
                lua_update()
            else:
                self.player.print(f"No update function found in Lua for Ant {self.ant_id}")
        except Exception as e:
            self.player.print(f"Error in Lua script for Nest: {e}")    

        for ant in self.ants:
            ant.update(lua_runtime)
    
    def _on_memory_shift(self, evicted_value):
        """
        Callback function for when memory shifts (when an item is evicted).
        This would notify Lua or handle any needed action when memory is full.
        """
        print(f"Memory shifted, evicted: {evicted_value}")
