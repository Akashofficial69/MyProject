import os
import json
import pytest
from myproject.config_writer import write_env, write_json, set_os_env


def test_write_env(tmp_path):
    config = {"key": "value"}
    file_path = tmp_path / ".env"
    write_env(config, file_path)
    with open(file_path, 'r') as file:
        assert file.read() == "key=value\n"


def test_write_json(tmp_path):
    config = {"key": "value"}
    file_path = tmp_path / "config.json"
    write_json(config, file_path)
    with open(file_path, 'r') as file:
        data = json.load(file)
        assert data == config


def test_set_os_env():
    config = {"key": "value"}
    set_os_env(config)
    assert os.getenv("key") == "value"
