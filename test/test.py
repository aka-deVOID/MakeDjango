import os
from sys import platform
def make_venv(path: str, packages: list[str]) -> bool:

    if platform == "linux" or platform == "linux2":
        os.system('bash autovenv.sh %s %s' % (path, packages))
    elif platform == "win32":
        ...
    print(platform)
