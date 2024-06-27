import os

import pytest
from myproject.config_manager import flatten_dict, read_config, write_config, set_config_env


def test_flatten_dict():
    nested = {"a": {"b": {"c": 1}}}
    flat = flatten_dict(nested)
    assert flat == {"a_b_c": 1}


def test_read_config():
    data = read_config('tests/test_files/test.yaml')
    assert data == {"key": "value"}


def test_write_config(tmp_path):
    config = {"key": "value"}
    file_path = tmp_path / ".env"
    write_config(config, file_path, 'env')
    with open(file_path, 'r') as file:
        assert file.read() == "key=value\n"


def test_set_config_env():
    config = {"key": "value"}
    set_config_env(config)
    assert os.getenv("key") == "value"

