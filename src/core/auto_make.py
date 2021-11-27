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
    "template/forms.py",
    "template/models.py",
    "template/tests.py",
    "template/urls.py",
    "template/views.py",
)

User_Files: tuple = (
    "template/__init__.py",
    "template/admin.py",
    "template/forms.py",
    "template/models.py",
    "template/permissions.py",
    "template/tests.py",
    "template/views.py",
    "template/authentications.py",
    "template/middlewares.py",
    "template/managers.py",
)

Rest_Files: tuple = (
    "template/__init__.py",
    "template/admin.py",
    "template/models.py",
    "template/urls.py",
    "template/tests.py",
    "template/views.py",
    "template/throttles.py",
    "template/serializers.py",

)

def create_apps(app_dir: str, app_name: str) -> None:
    """Creates the apps.py file."""

    code: str = f"""from django.apps import AppConfig

class {app_name.capitalize()}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{app_name}'

    """
    apps_file = open(join(app_dir, "apps.py"), 'w'); apps_file.write(code); apps_file.close()

def rest(apps: list, main_dir: str) -> bool:
    """Creating App Files For Rest mode"""
    for app in apps:
        app_dir = join(main_dir, app); mkdir(app_dir)
        migrations_dir = join(app_dir, "migrations"); mkdir(migrations_dir); copyfile(Base / "template/__init__.py", join(migrations_dir, "__init__.py"))
    
        if app in ("user", "account", "accounts"):
            create_apps(app_dir, app)
            for user_file in User_Files:
                copyfile(Base / user_file, join(app_dir, user_file[9:]))
            
            print(f"\33[32m==> {app.capitalize()} Craeted... \U00002705")
            continue
        
        create_apps(app_dir, app)
        for rest_file in Rest_Files:
            copyfile(Base / rest_file, join(app_dir, rest_file[9:]))
    
        print(f"\33[32m==> {app.capitalize()} Craeted... \U00002705")
    return True

def django(apps: list, main_dir: str) -> bool:
    """Creating App Files For Django(Jinja2) mode"""
    mkdir(join(main_dir, "templates")); mkdir(join(main_dir, "static"))
    for app in apps:
        app_dir = join(main_dir, app); mkdir(app_dir)
        migrations_dir = join(app_dir, "migrations"); mkdir(migrations_dir); copyfile(Base / "template/__init__.py", join(migrations_dir, "__init__.py"))

        if app in ("user", "account", "accounts"):
            create_apps(app_dir, app)
            for user_file in User_Files:
                copyfile(Base / user_file, join(app_dir, user_file[9:]))

            print(f"\33[32m==> {app.capitalize()} Craeted... \U00002705")
            continue

        mkdir(join(app_dir, f"templates")); mkdir(join(app_dir + "/templates", app))
        create_apps(app_dir, app)
        for django_file in Django_Files:
            copyfile(Base / django_file, join(app_dir, django_file[9:]))

        print(f"\33[32m==> {app.capitalize()} Craeted... \U00002705")
    return True

def graphql(apps: list, main_dir: str) -> bool:
    """Creating App Files For GraphQL mode"""
    # TODO: graphql
    ...
    return True

def auto(project_name: str, apps: list, framework: str, path: str) -> bool:
    """
    Creates default files. It then assigns the continuation to the function of each state.
    """

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

    if framework == "rest" and rest(apps, main_dir):
        return True
    elif framework == "django" and django(apps, main_dir):
        return True
    elif framework == "graphql" and graphql(apps, main_dir):
        return True
