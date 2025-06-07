import os
import json5
class ModManager:
    @staticmethod
    def load_mod_config(save_name):
        """
        Load mod configuration from mods.json if it exists.

        Args:
            save_name (str): The name of the save.

        Returns:
            list: A list of mod dictionaries with 'name', 'enabled', and 'load_order'.
        """
        mods_file_path = os.path.join("saves", save_name, "mods.json")
        if os.path.exists(mods_file_path):
            with open(mods_file_path, "r") as mods_file:
                return json5.load(mods_file)
        else:
            return []

    @staticmethod
    def scan_mods_folder():
        """
        Scan the mods folder for available mods.

        Returns:
            list: A list of mod names found in the mods folder.
        """
        mods_path = "mods"
        if not os.path.exists(mods_path):
            os.makedirs(mods_path)
            return []
        return [mod for mod in os.listdir(mods_path) if os.path.isdir(os.path.join(mods_path, mod))]

    @staticmethod
    def get_mod_status(mods_config, available_mods):
        """
        Determine active and inactive mods based on configuration and available mods.
    
        Args:
            mods_config (list): The list of mods from mods.json.
            available_mods (list): The list of mods available in the mods folder.
    
        Returns:
            tuple: (active_mods, inactive_mods)
        """
        # If mods_config is empty, treat all available mods as inactive
        if not mods_config:
            return [], available_mods
    
        active_mods = [mod for mod in mods_config if mod in available_mods]
        inactive_mods = [mod for mod in available_mods if mod not in [m for m in mods_config]]
        inactive_mods.sort()
        return active_mods, inactive_mods

