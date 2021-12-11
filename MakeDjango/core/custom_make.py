import os
import sys
from pyfiglet import Figlet
from PyInquirer import style_from_dict, Token, prompt, Separator
from os import mkdir
from os.path import join
from shutil import copyfile
from .auto_make import create_apps, Base, Setup_Files

style = style_from_dict({
    Token.Separator: '#4fff00',
    Token.QuestionMark: '#ff0000 bold',
    Token.Selected: '#2986cc',
    Token.Pointer: '#ffec00 bold',
    Token.Instruction: '#ffffff',
    Token.Answer: '#274e13 bold',
    Token.Question: '#c90076',
})

def header(name: str, apps: list, framework: str, path: str) -> None:
    text_seting = Figlet(font='doom')
    print(f"\33[32m{text_seting.renderText('MakeDjango')}")
    print("_"*55)
    print(f"Project Name: \'{name}\'")
    print(f"Apps: {[ i for i in apps]}")
    print(f"Mode: \'{framework}\'")
    if os.getcwd() == path:
        print("Path: \'./here\'")
    else:
        print(f"Path: \'{path}\'")
    print("_"*55)

def selected_app_files() -> dict:
    questions = [
        {
            'type': 'checkbox',
            'message': '=> Select app files:',
            'name': 'apps',
            'choices': [
                Separator('=> All Apps <='),
                {'name': '__init__.py', 'checked': True},
                {'name': 'admin.py'}, {'name': 'forms.py'},
                {'name': 'utils.py'}, {'name': 'signals.py'},
                {'name': 'tests.py'}, {'name': 'urls.py'},
                {'name': 'views.py'}, {'name': 'throttles.py'},
                {'name': 'serializers.py'}, {'name': 'schema.py'},
                {'name': 'models.py'}, {'name': 'querysets.py'},
            ],
            'validate': lambda answer: 'You probably forgot something ...' if len(answer) == 0 else True
        },
        {
            'type': 'checkbox',
            'message': '=> Select user-app file:',
            'name': 'user',
            'choices': [
                Separator('=> User App <='),
                {'name': '__init__.py', 'checked': True},
                {'name': 'forms.py'}, {'name': 'models.py'},
                {'name': 'utils.py'}, {'name': 'signals.py'},
                {'name': 'permissions.py'}, {'name': 'tests.py'},
                {'name': 'views.py'}, {'name': 'authentications.py'},
                {'name': 'middlewares.py'}, {'name': 'schema.py'},
                {'name': 'throttles.py'}, {'name': 'serializers.py'},
                {'name': 'admin.py'}, {'name': 'querysets.py'},
            ],
            'validate': lambda answer: 'You probably forgot something ...' if len(answer) == 0 else True
        }
    ]
    return prompt(questions, style=style)

def choice_user_app(apps: list) -> dict:
    questions = [
        {
            'type': 'list',
            'name': 'user',
            'message': '=> Which is your user file?',
            'choices': apps,
        },
    ]
    return prompt(questions, style=style)

def custom(name: str, apps: list, framework: str, path: str) -> bool:
    header(name, apps, framework, path)
    user_app: dict = choice_user_app(apps)
    files: dict = selected_app_files()
    main_dir: str = join(path, name)
    setup_dir: str = join(main_dir, name)

    try:
        mkdir(main_dir); mkdir(setup_dir)
    except FileExistsError:
        sys.exit("MakeDjango: There is a folder with the project name.")

    copyfile(Base / "template/manage.py", join(main_dir, "manage.py"))

    for setup_file in Setup_Files:
        copyfile(Base / setup_file, join(setup_dir, setup_file[9:]))

    print("\33[32m==> Project Created... \U00002705")

    for app in apps:
        app_dir = join(main_dir, app); mkdir(app_dir)
        migrations_dir = join(app_dir, "migrations"); mkdir(migrations_dir); copyfile(Base / "template/__init__.py", join(migrations_dir, "__init__.py"))
        if app == user_app["user"]:
            create_apps(app_dir, app)
            for _file in files["user"]:
                copyfile(Base / join("template/", _file), join(app_dir, _file))
            
            print(f"\33[32m==> {app.capitalize()} Craeted... \U00002705")
            continue

        create_apps(app_dir, app)
        for _file in files["apps"]:
            copyfile(Base / join("template", _file), join(app_dir, _file))
        print(f"\33[32m==> {app.capitalize()} Craeted... \U00002705")
    return True