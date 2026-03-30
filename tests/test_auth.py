from src.security.auth import authenticate
import pytest

def test_authentication_success():
    assert authenticate('admin', 'password') is True

def test_authentication_failure():
    assert authenticate('user', 'wrong_password') is False
