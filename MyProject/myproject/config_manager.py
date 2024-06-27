from .config_reader import read_yaml, read_cfg, read_conf
from .config_writer import write_env, write_json, set_os_env


def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def read_config(file_path):
    if file_path.endswith('.yaml'):
        return read_yaml(file_path)
    elif file_path.endswith('.cfg') or file_path.endswith('.conf'):
        return read_cfg(file_path)
    else:
        raise ValueError("Unsupported file format")


def write_config(config_dict, file_path, file_format):
    flat_config = flatten_dict(config_dict)
    if file_format == 'env':
        write_env(flat_config, file_path)
    elif file_format == 'json':
        write_json(flat_config, file_path)
    else:
        raise ValueError("Unsupported file format")


def set_config_env(config_dict):
    flat_config = flatten_dict(config_dict)
    set_os_env(flat_config)
