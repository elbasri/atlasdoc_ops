from src.security.roles import get_user_roles
import pytest

def test_admin_roles():
    roles = get_user_roles('admin')
    assert 'admin' in roles

def test_regular_user_roles():
    roles = get_user_roles('user')
    assert not roles
