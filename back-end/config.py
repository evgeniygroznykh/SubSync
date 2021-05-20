import os
import json
from json import JSONDecodeError


CONFIG_JSON_FILE_NAME = 'config.json'
ROOT_PY_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

CONFIG_FILE_PATH = f'{ROOT_PY_DIRECTORY}\\{CONFIG_JSON_FILE_NAME}'

def read_config():
    try:
        with open(CONFIG_FILE_PATH) as json_config_file:
            provider_config = json.load(json_config_file)
        return provider_config
    except JSONDecodeError:
        return 'Error: config.json file is incorrect.'
    except FileNotFoundError:
        return 'Error: No config.json file was found.'
    except Exception:
        return 'Error: Reading of config.json file failed.'

def save_config(json_config):
    try:
        with open(CONFIG_FILE_PATH) as json_config_file:
            json.dump(json_config, json_config_file, ensure_ascii=False, indent=4)
    except Exception:
        return 'No config.json file was found'

PROVIDER_CONFIG = read_config()