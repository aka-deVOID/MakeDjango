import os
import sys
import subprocess
from pathlib import Path

here = Path(__file__).resolve().parent

def venv(path: str, packages: list[str]) -> bool:
    if sys.platform == "linux":
        str_package = " ".join(packages)
        
        os.system("bash %s %s %s" % (here / "linux.sh", str_package, path))
        return True

    elif sys.platform == "win32":
        str_package = " ".join(packages)
        bat_file = here / "win32.bat"
        subprocess.call([r'{}'.format(bat_file), str_package, path])
        return True