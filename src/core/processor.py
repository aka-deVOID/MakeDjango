from .auto_make import auto
from .custom_make import custom
import argparse
import os
import sys
import pathlib
import re

__version__: str = "0.0.0"

class Main:
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
    def path(self) -> str:
        return self._path
    
    @path.setter
    def path(self, path_addr: str) -> None:
        if os.path.isdir(path_addr):
            self._path = path_addr
        else:
            self.parser.error("The entered path is invalid")

    @property
    def apps(self):
        return self._apps

    @apps.setter
    def apps(self, app_names: list) -> None:
        regex = re.compile(r'([A-Za-z0-9\_])*')
        for item in app_names:
            if not re.fullmatch(regex, item):
                self.parser.error(f"Invalid Name: {item}")
        self._apps = app_names

    def processor(self) -> None:
        if self.auto:
            auto(self.name, self.apps, self.framework, self.path)
        elif self.custom:
            custom(self.name, self.apps, self.framework, self.path)
        elif self.version:
            print(f"Django Smithing Tools Version: {__version__}")
