import os
import sys
import subprocess

def venv(path: str, packages: list[str]) -> bool:
    if sys.platform == "linux":
        str_package = " ".join(packages)
        
        ...
    elif sys.platform == "win32":
        str_package = " ".join(packages)
        ...