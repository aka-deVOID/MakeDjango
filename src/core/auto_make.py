import os
import sys

def path_connector(base_path: str, *wargs: str) -> str:
    return os.path.join(base_path, *wargs)

def auto(project_name: str, apps: list, framework: str, path: str) -> None:
    main_dir = path_connector(path, project_name)
    try:
        os.mkdir(main_dir)
    except:
        sys.exit("Error when create directory")
    
