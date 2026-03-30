# temp_staging.py
import os
from typing import List

def get_temp_dir() -> str:
    return "temp_staging"

def list_files_in_temp_dir(temp_dir: str) -> List[str]:
    return os.listdir(temp_dir)
