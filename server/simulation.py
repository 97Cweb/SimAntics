import time
import threading

from queue import Queue

class Simulation:
    def __init__(self):
        self.game_state = {"nests": [], "ants": [], "resources": []}
        self.running = False
        self.command_queue = Queue()

    def start(self):
        """Start the simulation loop in a separate thread."""
        self.running = True
        simulation_thread = threading.Thread(target=self.run, daemon=True)
        simulation_thread.start()

    def stop(self):
        """Stop the simulation."""
        self.running = False

    def run(self):
        """Run the simulation loop."""
        print("Simulation started.")
        while self.running:
            self.update()
            time.sleep(0.1)  # Adjust the tick rate (e.g., 10 ticks per second)

    def update(self):
        """Run one tick of the game simulation."""
        print("Simulating one game tick...")
        # Add simulation logic here

# Singleton simulation instance
simulation_instance = Simulation()
