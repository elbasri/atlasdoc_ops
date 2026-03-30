# test_versioning.py

from src.versioning import get_version

def test_get_version():
    assert get_version() == '1.0.0'
