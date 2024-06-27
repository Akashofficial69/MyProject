import yaml
import configparser


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def read_cfg(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return {section: dict(config.items(section)) for section in config.sections()}


def read_conf(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return {section: dict(config.items(section)) for section in config.sections()}
