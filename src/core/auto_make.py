import sys
from pathlib import Path
from os import mkdir
from os.path import join
from shutil import copyfile

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
    #"template/forms.py",
    "template/models.py",
    "template/tests.py",
    "template/views.py"
)

def create_apps(app_dir: str, app_name: str) -> None:
    code: str = f"""from django.apps import AppConfig

class {app_name.capitalize()}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{app_name}'

    """
    apps_file = open(join(app_dir, "apps.py"), 'w'); apps_file.write(code)

def rest(apps: list) -> None:
    ...

def django(apps: list, main_dir: str) -> None:
    for app in apps:
        if app in ("user", "account", "accounts"):
            ...
            continue

        app_dir = join(main_dir, app); mkdir(app_dir)
        migrations_dir = join(app_dir, "migrations"); mkdir(migrations_dir); copyfile(Base / "template/__init__.py", join(migrations_dir, "__init__.py"))
        
        for django_file in Django_Files:
            create_apps(app_dir, app)
            copyfile(Base / django_file, join(app_dir, django_file[9:]))

        print(f"\33[32m==> {app.capitalize()} Craeted... \U00002705")

    print("\33[32m==> Done... \U00002705")

def graphql(apps: list) -> None:
    ...

def auto(project_name: str, apps: list, framework: str, path: str) -> None:
    main_dir: str = join(path, project_name)
    setup_dir: str = join(main_dir, project_name)

    try:
        mkdir(main_dir); mkdir(setup_dir)
    except FileExistsError:
        sys.exit("DST: " + "There is a folder with the project name")

    copyfile(Base / "template/manage.py", join(main_dir, "manage.py"))

    for setup_file in Setup_Files:
        copyfile(Base / setup_file, join(setup_dir, setup_file[9:]))

    print("\33[32m==> Project Created... \U00002705")

    if framework == "rest":
        rest(apps)
    elif framework == "django":
        django(apps, main_dir)
    elif framework == "graphql":
        graphql(apps)
