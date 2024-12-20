import os
import shutil
import json5
from collections import deque

from player import Player
from nest import Nest
from ant import Ant

from server import Server



class SimulationSaver:
    @staticmethod
    def create_save_folder(simulation, save_name):
        save_path = os.path.join("saves", save_name)
        os.makedirs(save_path, exist_ok=True)
        if simulation.save_name != save_name:
            players_src = os.path.join("saves", simulation.save_name,"players")
            players_dest = os.path.join("saves", save_name, "players")
            if os.path.exists(players_src):
                shutil.copytree(players_src, players_dest, dirs_exist_ok = True)
    
        return save_path


    @staticmethod
    def save_simulation(simulation, save_name):
        save_path = SimulationSaver.create_save_folder(simulation, save_name)

        SimulationSaver._save_simulation_attributes(simulation, save_path)
        SimulationSaver._save_server_attributes(simulation, save_path)
        SimulationSaver._save_terrain_grid(simulation, save_path)
        SimulationSaver._save_pheromone_grid(simulation, save_path)
        SimulationSaver._save_players(simulation, save_path)
        SimulationSaver._save_mods_config(simulation, save_path)

        print(f"Simulation saved to {save_path}")

    @staticmethod
    def _save_simulation_attributes(simulation, save_path):
        simulation_data = {
            "map_update_interval": simulation.map_update_interval,
            "gas_update_interval": simulation.gas_update_interval,
            "max_player_gas_count": simulation.pheromone_manager.max_player_gas_count,
        }
        with open(os.path.join(save_path, "simulation.json"), "w") as sim_file:
            json5.dump(simulation_data, sim_file, indent=4)
         
        staticmethod
    def _save_server_attributes(simulation, save_path):
        if simulation.server:
            server_data = {
                "host": simulation.server.host,
                "port": simulation.server.port,
                "udp_port": simulation.server.udp_port,
                "inactivity_timeout": simulation.server.inactivity_timeout,
                "message_interval_rate": simulation.server.message_throttler.interval,
            }
            with open(os.path.join(save_path, "server.json"), "w") as server_file:
                json5.dump(server_data, server_file, indent=4)
    
    
    @staticmethod
    def _save_terrain_grid(simulation, save_path):
        terrain_data = [[dict(cell) for cell in row] for row in simulation.terrain_grid.grid]
        with open(os.path.join(save_path, "terrain.json"), "w") as terrain_file:
            json5.dump(terrain_data, terrain_file, indent=4)
    
    @staticmethod
    def _save_pheromone_grid(simulation, save_path):
       pheromone_data = {
           "grid": simulation.pheromone_manager.grid,
           "pheromone_definitions": simulation.pheromone_manager.pheromone_definitions,
           "uuid_to_pheromone": simulation.pheromone_manager.uuid_to_pheromone,
       }
       with open(os.path.join(save_path, "pheromones.json"), "w") as pheromone_file:
           json5.dump(pheromone_data, pheromone_file, indent=4)
    
    @staticmethod
    def _save_players(simulation, save_path):
        players_data = {}
        for player in simulation.players.values():
            players_data[player.username] = {
                "is_human": player.is_human,
                "nests": [
                    {
                        "x": nest.x,
                        "y": nest.y,
                        "memory": list(nest.memory.memory),
                        "ants": [
                            {
                                "x": ant.x,
                                "y": ant.y,
                                "max_speed": ant.max_speed,
                                "memory": list(ant.memory.memory),
                            }
                            for ant in nest.ants
                        ],
                    }
                    for nest in player.nests
                ],
            }
        with open(os.path.join(save_path, "players.json"), "w") as players_file:
            json5.dump(players_data, players_file, indent=4)
    
    
    
    @staticmethod
    def _save_mods_config(simulation, save_path):
        """
        Save the enabled mods configuration to mods.json.
    
        Args:
            simulation: The simulation instance containing the enabled mods.
            save_path: The path to the save directory.
        """
        mods_file_path = os.path.join(save_path, "mods.json")
        with open(mods_file_path, "w") as mods_file:
            json5.dump(simulation.enabled_mods, mods_file, indent=4)
        print(f"Mods configuration saved to {mods_file_path}")
    
    
    def load_simulation_config(save_name):
        save_path = os.path.join("saves", save_name)
        simulation_data = SimulationSaver._load_simulation_attributes(save_path, save_name)
        server_data = SimulationSaver._load_server_attributes(save_path)
        mods_data = SimulationSaver._load_mods_list(save_name)
        return simulation_data, server_data, mods_data
        
    def load_simulation(simulation, save_name):
        save_path = os.path.join("saves", save_name)
        SimulationSaver._load_terrain_grid(simulation, save_path)
        SimulationSaver._load_pheromone_grid(simulation, save_path)
        SimulationSaver._load_players(simulation, save_path, save_name)
        

        print(f"Simulation loaded from {save_path}")    
        
    @staticmethod
    def _load_simulation_attributes(save_path, save_name):
        with open(os.path.join(save_path, "simulation.json"), "r") as sim_file:
            simulation_data = json5.load(sim_file)
            simulation_data["save_name"] = save_name
            simulation_data["x"] = "from save"
            simulation_data["y"] = "from save"
            return simulation_data

    
       
    @staticmethod
    def _load_server_attributes(save_path):
        server_file_path = os.path.join(save_path, "server.json")
        if os.path.exists(server_file_path):
            with open(server_file_path, "r") as server_file:
                server_data = json5.load(server_file)
                return server_data
            
    @staticmethod
    def _load_terrain_grid(simulation, save_path):
        with open(os.path.join(save_path, "terrain.json"), "r") as terrain_file:
            terrain_data = json5.load(terrain_file)
            simulation.terrain_grid.grid = [
                [simulation.terrain_grid.lua.table_from(cell) for cell in row]
                for row in terrain_data
            ]

    
    @staticmethod
    def _load_pheromone_grid(simulation, save_path):
        with open(os.path.join(save_path, "pheromones.json"), "r") as pheromone_file:
            pheromone_data = json5.load(pheromone_file)
            simulation.pheromone_manager.grid = pheromone_data["grid"]
            simulation.pheromone_manager.pheromone_definitions = pheromone_data["pheromone_definitions"]
            simulation.pheromone_manager.uuid_to_pheromone = pheromone_data["uuid_to_pheromone"]

    @staticmethod
    def _load_players(simulation, save_path, save_name):
        with open(os.path.join(save_path, "players.json"), "r") as players_file:
            players_data = json5.load(players_file)
            simulation.players = {}
    
            for username, player_data in players_data.items():
                player = Player(
                    username=username,
                    save_name=save_name,
                    pheromone_manager=simulation.pheromone_manager,
                    message_callback=simulation.message_callback,
                    is_human=player_data["is_human"]
                )
                    
                simulation.players[username] = player

                player.pheromone_definitions = player_data["pheromone_definitions"]
                
                
                # Load nests
                for nest_data in player_data["nests"]:
                    nest = Nest(
                        player=player,
                        pheromone_manager=simulation.pheromone_manager,
                        memory_size=len(nest_data["memory"]),
                        x=nest_data["x"],
                        y=nest_data["y"],
                    )
                    nest.memory.memory = deque(nest_data["memory"], maxlen=nest.memory.max_len)
                    player.nests.append(nest)
                    
                    # Load ants
                    for ant_data in nest_data["ants"]:
                        ant = Ant(
                        player=player,
                        pheromone_manager=simulation.pheromone_manager,
                        x=ant_data["x"],
                        y=ant_data["y"],
                        max_speed=ant_data["max_speed"],
                        memory_size=len(ant_data["memory"]),
                    )
                    ant.memory.memory = deque(ant_data["memory"], maxlen=ant.memory.max_len)
                    nest.ants.append(ant)
                    
                    
                player._initialize_lua_environment()
        print(f"Simulation loaded from {save_path}")
        


    @staticmethod
    def _load_mods_list(save_name):
        """
        Load the enabled mods configuration from mods.json.
    
        Args:
            simulation: The simulation instance to update with the enabled mods.
            save_path: The path to the save directory.
        """
        mods_file_path = os.path.join("saves", save_name, "mods.json")
        if os.path.exists(mods_file_path):
            with open(mods_file_path, "r") as mods_file:
                mod_list = json5.load(mods_file)
                enabled_mods = [mod for mod in mod_list if mod["enabled"]]

                print(f"Mods configuration loaded from {mods_file_path}")

                return enabled_mods
                
        else:
            print(f"No mods.json found in {save_name}. Defaulting to all mods enabled.")
            return []
            
            
    @staticmethod
    def create_player_folder(save_name,username):
        """Create a folder for the player and generate their Lua scripts."""
        players_path = os.path.join("saves", save_name, "players")
        
        templates_path = os.path.join("lua", "templates")
        player_template_path = os.path.join(templates_path, "PlayerA")
        
        # Ensure the templates folder exists
        if not os.path.exists(player_template_path):
           raise FileNotFoundError(f"Template folder {player_template_path} does not exist.")

        # Copy the template directory to the player's folder
        intermediate_path = os.path.join(players_path, username) 
        shutil.copytree(player_template_path, intermediate_path, dirs_exist_ok = True)
        
        

        print(f"Player folder created for {username}")