import threading
from collections import deque

# AntMemory class from above (simplified for clarity)
class Memory:
    def __init__(self, max_len=32, default_value=None, shift_callback=None):
        self.max_len = max_len
        self.shift_callback = shift_callback
        self.memory = deque([default_value] * max_len, maxlen=max_len)
        self.lock = threading.Lock()  # Add a lock for thread safety

    def __getitem__(self, index):
        return self.memory[index]

    def getitem(self, index):
        """
        Lua-friendly method to access items by index.
        Simply calls the __getitem__ method.
        """
        return self.__getitem__(index)
    
    def __setitem__(self, index, value):
        if not self._validate_value(value):
            return
        self.memory[index] = value
        
    def setitem(self, index, value):
        """
        Lua-friendly method to set items at a specific index.
        Simply calls the __setitem__ method.
        """
        return self.__setitem__(index, value)

    def add(self, value):
        if not self._validate_value(value):
            return
        with self.lock:
            if len(self.memory) == self.max_len:
                if self.shift_callback:
                    self.shift_callback(self.memory[0])  # Notify Lua of eviction
            self.memory.append(value)
        
    def shift(self):
        with self.lock:
            if self.memory:
                evicted_item = self.memory.popleft()
                if self.shift_callback:
                    self.shift_callback(evicted_item)
                return evicted_item
            return None
        
    def _validate_value(self, value):
        """
        Ensure the value is a valid type: int, float, str, or None.
        Returns True if valid, False otherwise.
        """
        return isinstance(value, (int, float, str, type(None)))