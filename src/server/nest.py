from memory import Memory
from ant import Ant
class Nest:
    def __init__(self, memory_size = 128, position = (0,0), spawn_callback=None):
        self.position = (0, 0)  # Default position
        self.memory = Memory(max_len=memory_size, default_value=None, shift_callback=self._on_memory_shift)
        self.spawn_callback = spawn_callback  # Callback to spawn ants into the simulation
        self.ants = []
        
        self.spawn_ant()
    
    def smell(self):
        """Simulate nest smelling."""
        print("nest {self.nest_id} is smelling surroundings")
        return []

    def spawn_ant(self):
        """Spawn a new Ant and notify the simulation."""
        new_ant = Ant(position=self.position)
        self.ants.append(new_ant)
        if self.spawn_callback:
            self.spawn_callback(new_ant)
            print(f"Nest spawned Ant")
       
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
                print(f"No update function found in Lua for Ant {self.ant_id}")
        except Exception as e:
            print(f"Error in Lua script for Ant {self.ant_id}: {e}")    

        for ant in self.ants:
            ant.update(lua_runtime)
    
    def _on_memory_shift(self, evicted_value):
        """
        Callback function for when memory shifts (when an item is evicted).
        This would notify Lua or handle any needed action when memory is full.
        """
        print(f"Memory shifted, evicted: {evicted_value}")
