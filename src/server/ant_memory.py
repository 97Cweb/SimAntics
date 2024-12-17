from collections import deque

# AntMemory class from above (simplified for clarity)
class AntMemory:
    def __init__(self, max_len=32, default_value=None, shift_callback=None):
        self.max_len = max_len
        self.shift_callback = shift_callback
        self.memory = deque([default_value] * max_len, maxlen=max_len)

    def __getitem__(self, index):
        return self.memory[index]

    def __setitem__(self, index, value):
        self.memory[index] = value

    def __len__(self):
        return len(self.memory)
    
    def __iter__(self):
        return iter(self.memory)

    def add(self, value):
        if len(self.memory) == self.max_len:
            if self.shift_callback:
                self.shift_callback(self.memory[0])  # Notify Lua of eviction
        self.memory.append(value)
        
    def shift(self):
        if self.memory:
            evicted_item = self.memory.popleft()
            if self.shift_callback:
                self.shift_callback(evicted_item)