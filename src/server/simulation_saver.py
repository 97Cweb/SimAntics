import os
import json5


class SimulationSaver:
    @staticmethod
    def create_save_folder(save_name):
        save_path = os.path.join("saves", save_name)
        os.makedirs(save_path, exist_ok=True)
        return save_path

    @staticmethod
    def save(save_name, frame_counter, mods, grid, gas_grid, players):
        save_path = SimulationSaver.create_save_folder(save_name)
        save_data = {
            "version": "0.0.1",
            "frame_counter": frame_counter,
            "mods": mods,
            "simulation_state": {
                "grid": SimulationSaver.format_grid(grid),
                "gas_grid": SimulationSaver.format_grid(gas_grid),
                "players": players,
            },
        }
        with open(os.path.join(save_path, "sim.json"), "w") as f:
            json5.dump(save_data, f, indent=4)
        print(f"Game saved to {save_path}")

    @staticmethod
    def load(lua_runtime, save_name):
        save_path = os.path.join("saves", save_name, "sim.json")
        if not os.path.exists(save_path):
            raise FileNotFoundError(f"No save file found for {save_name}")

        with open(save_path, "r") as f:
            save_data = json5.load(f)

        # Restore grids and other states
        frame_counter = save_data["frame_counter"]
        grid = SimulationSaver.load_grid(lua_runtime, save_data["simulation_state"]["grid"])
        gas_grid = SimulationSaver.load_grid(lua_runtime, save_data["simulation_state"]["gas_grid"])
        players = save_data["simulation_state"]["players"]

        return frame_counter, grid, gas_grid, players

    @staticmethod
    def format_grid(grid):
        """Convert the grid to a human-readable format."""
        return [
            [{key: cell[key] for key in cell} for cell in row]
            for row in grid
        ]

    @staticmethod
    def load_grid(lua_runtime, formatted_grid):
        """Recreate Lua tables from the formatted grid."""
        return [
            [lua_runtime.table_from(cell) for cell in row]
            for row in formatted_grid
        ]
