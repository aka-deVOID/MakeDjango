import os
import sys
from pathlib import Path
import shutil

Base: str = Path(__file__).resolve().parent.parent

Setup_Files: tuple = (
    "template/__init__.py",
    "template/asgi.py",
    "template/wsgi.py",
    "template/settings.py",
    "template/urls.py",
)

Django_Files: tuple = (
    "template/__init__.py",
    "template/admin.py",
    "template/apps.py",
    "template/models.py",
    "template/tests.py",
    "template/views.py"
)

def pc(base_path: str, *wargs: str) -> str:
    return os.path.join(base_path, *wargs)

def rest(apps: list) -> None:
    ...

def django(apps: list, main_dir: str) -> None:
    for app in apps:
        ...
    print("\33[32m==> Done... \U00002705")

def graphql(apps: list) -> None:
    ...

def auto(project_name: str, apps: list, framework: str, path: str) -> None:
    main_dir: str = pc(path, project_name)
    setup_dir: str = pc(main_dir, project_name)

    try:
        os.mkdir(main_dir); os.mkdir(setup_dir)
    except FileExistsError:
        sys.exit("DST: " + "There is a folder with the project name")

    shutil.copyfile(Base / "template/manage.py", pc(main_dir, "manage.py"))

    for setup_file in Setup_Files:
        shutil.copyfile(Base / setup_file, pc(setup_dir, setup_file[9:]))

    print("\33[32m==> Project Created... \U00002705")

    if framework == "rest":
        rest(apps)
    elif framework == "django":
        django(apps, main_dir)
    elif framework == "graphql":
        graphql(apps)
