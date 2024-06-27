import json
import os


def write_env(config_dict, file_path):
    with open(file_path, 'w') as file:
        for key, value in config_dict.items():
            file.write(f"{key}={value}\n")


def write_json(config_dict, file_path):
    with open(file_path, 'w') as file:
        json.dump(config_dict, file, indent=4)


def set_os_env(config_dict):
    for key, value in config_dict.items():
        os.environ[key] = str(value)
