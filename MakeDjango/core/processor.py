import os
import re
import argparse
from .auto_make import auto
from .custom_make import custom

__version__: str = "0.0.1"

class Main:
    """Validates argparse values. It then calls the required function based on the flag (-a | -c)."""

    def __init__(self, parser, **kwargs) -> None:
        self.parser: isinstance(argparse) = parser
        self.version: str = kwargs["version"]
        self.auto: bool = kwargs["auto"]; self.custom: bool = kwargs["custom"]
        self.name: str = kwargs["name"]
        self.path: str = kwargs["path"]
        self.framework: str = kwargs["framework"]
        self.apps: list = kwargs["appnames"]
        self.processor()

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __repr__(self) -> str:
        return f"{__class__}"
    
    @property
    def name(self) -> str:
        self._name

    @property
    def path(self) -> str:
        return self._path
            
    @property
    def apps(self) -> str:
        return self._apps

    @path.setter
    def path(self, path_addr: str) -> None:
        if os.path.isdir(path_addr):
            self._path = path_addr
        else:
            self.parser.error("The entered path is invalid")
    
    @name.setter
    def name(self, project_name: str) -> None:
        regex = re.compile(r'([A-Za-z0-9\_])*')
        if not re.fullmatch(regex, project_name):
            self.parser.error("Invalid project name")
        else:
            self._name = project_name

    @apps.setter
    def apps(self, app_names: list) -> None:
        regex = re.compile(r'([A-Za-z0-9\_])*')
        for item in app_names:
            if not re.fullmatch(regex, item):
                self.parser.error(f"Invalid Name: {item}")
        self._apps = app_names

    def processor(self) -> None:
        if self.auto:
            if auto(self._name, self._apps, self.framework, self.path):
                print("\33[32m==> Done... \U00002705")
        elif self.custom:
            if custom(self._name, self._apps, self.framework, self.path):
                print("\33[32m==> Done... \U00002705")

class Other:
    """Processes other commands"""

    def __init__(self, version: bool) -> None:
        self.version: bool = version
        

