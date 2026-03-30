from typing import Any, Dict

def authenticate(user: str, password: str) -> bool:
    """
    Authenticate a user with a given password.
    
    Args:
        user (str): The username of the user.
        password (str): The password of the user.
    
    Returns:
        bool: True if authentication is successful, False otherwise.
    """
    # Placeholder for actual authentication logic
    return user == 'admin' and password == 'password'
