import os
import json


root_py_directory = os.path.dirname(os.path.realpath(__file__))
CONFIG_FILE_PATH = f'{root_py_directory}\\config.json'

def read_config():
    print(CONFIG_FILE_PATH)
    try:
        with open(CONFIG_FILE_PATH) as json_config_file:
            provider_config = json.load(json_config_file)
        return provider_config
    except Exception as exc:
        print(exc)
        return 'No config.json file was found.'


PROVIDER_CONFIG = read_config()