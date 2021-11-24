class Main():
    def __init__(self, **kwargs) -> None:
        self.version = kwargs["version"]
        self.auto = kwargs["auto"]
        self.custom = kwargs["custom"]
        self.name = kwargs["name"]
        self.path = kwargs["path"]
        self.framework = kwargs["framework"]

    # TODO: complete class