from .auto_make import auto
from .custom_make import custom

__version__: str = "0.0.0"

class Main:
    def __init__(self, **kwargs) -> None:
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

    def processor(self) -> None:
        if self.auto:
            auto(self.name, self.apps, self.framework, self.path)
        elif self.custom:
            custom(self.name, self.apps, self.framework, self.path)
        elif self.version:
            print(f"Django Smithing Tools Version: {__version__}")
