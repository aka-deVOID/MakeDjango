import pathlib
import os
import sys

def path_connector(base_path: str, **kwargs: str) -> str:
    return os.path.join(base_path, *kwargs)

def auto(project_name: str, apps: list, framework: str, path: str) -> None:
    os.mkdir(path / project_name)
