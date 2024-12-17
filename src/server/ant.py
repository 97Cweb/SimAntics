import math 
import random

from memory import Memory
class Ant:
    def __init__(self, player, pheromone_manager, x = 0, y =0, max_speed=1.0, memory_size = 32):
        self.player = player
        self.pheromone_manager = pheromone_manager
        self.x = x
        self.y = y
        self.direction = random.uniform(0, 2*math.pi)      # Default facing direction
        self.speed = 0
        self.max_speed = max_speed
        self.memory = Memory(max_len=memory_size, default_value=None, shift_callback=self._on_memory_shift)

    def see(self, degrees, distance):
        """Simulate ant vision."""
        print(f"Ant {self.ant_id} sees within {degrees} degrees and {distance} distance.")
        return []  # Example: Return empty vision for now
    
    def smell(self):
        """Simulate ant smelling."""
        print("ant {self.ant_id} is smelling surroundings")
        return []
    
    def emit_pheromone(self, pheromone_name, amount):
        pheromone_uuid = self.pheromone_manager.get_pheromone_uuid(self.player.username, pheromone_name)
        if pheromone_uuid:
            self.pheromone_manager.emit_pheromone(self.x, self.y, pheromone_uuid, amount)
        else:
            print(f"[Warning] Pheromone '{pheromone_name}' not registered for player {self.player.username}.")
    
    def set_velocity(self, magnitude, rel_angle ):
        """Set the movement of the ant."""
        self.direction = rel_angle
        self.speed = min(max(magnitude, 0.0), 1.0)
        print(f"Ant moving at {self.speed} speed and {self.direction} direction.")

    def update(self, lua_runtime):
        """Update ant behavior using the Lua script."""
        
        try:
            # Create Lua runtime globals and expose Python methods
            lua_globals  = lua_runtime.globals()
            
            base_ant_table = lua_globals.Base_Ant
            if base_ant_table is None:
                raise ValueError("Base_Ant not found in Lua globals.")
                
            # Set specific Python functions as attributes of Base_Ant
            base_ant_table.see = self.see
            base_ant_table.smell = self.smell
            base_ant_table.emit_pheromone = self.emit_pheromone
            base_ant_table.set_velocity = self.set_velocity
        
    
    
            # Provide controlled access to memory (read/write, no expansion)
            base_ant_table.memory = {
           "get": self.memory.getitem,
           "set": self.memory.setitem,
           "add": self.memory.add,
           "shift": self.memory.shift,
           
       }
    
            
            # Call the Lua script's "update" function
            lua_update = base_ant_table.update  # Don't call it yet (no parentheses)
            if lua_update:
                lua_update()
            else:
                print(f"No update function found in Lua for Ant {self.ant_id}")
        except Exception as e:
            print(f"Error in Lua script for Ant: {e}")    

    
    def _on_memory_shift(self, evicted_value):
        """
        Callback function for when memory shifts (when an item is evicted).
        This would notify Lua or handle any needed action when memory is full.
        """
        print(f"Memory shifted, evicted: {evicted_value}")


    def move(self, magnitude, direction ):
        """
        A method to move the ant (called by Lua).
        """
        self.x += magnitude * math.cos(direction)
        self.y += magnitude * math.sin(direction)