import os
import yaml

# Load the configuration file
config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')

def load_config():
    """
    Loads the configuration settings from the config.yaml file.

    Returns:
        dict: Configuration data as a dictionary.
    """
    with open(config_path, 'r') as config_file:
        return yaml.safe_load(config_file)

# Initialize a global config dictionary to use across the application
config = load_config()