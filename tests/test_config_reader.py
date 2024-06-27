import pytest
from myproject.config_reader import read_yaml, read_cfg, read_conf


def test_read_yaml():
    data = read_yaml('tests/test_files/test.yaml')
    assert data == {"key": "value"}


def test_read_cfg():
    data = read_cfg('tests/test_files/test.cfg')
    assert data == {"section": {"key": "value"}}


def test_read_conf():
    data = read_conf('tests/test_files/test.conf')
    assert data == {"section": {"key": "value"}}


