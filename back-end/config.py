import os
import json


root_py_directory = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE_PATH = f'{root_py_directory}\\config.json'

def read_config():
    try:
        with open(CONFIG_FILE_PATH) as json_config_file:
            provider_config = json.load(json_config_file)
        return provider_config
    except Exception:
        return 'No config.json file was found.'

def save_config(json_config):
    try:
        with open(CONFIG_FILE_PATH) as json_config_file:
            json.dump(json_config, json_config_file, ensure_ascii=False, indent=4)
    except Exception:
        return 'No config.json file was found'

PROVIDER_CONFIG = read_config()