class Main():
    def __init__(self, **kwargs) -> None:
        self.version = kwargs["version"]
        self.auto = kwargs["auto"]
        self.custom = kwargs["custom"]
        print(kwargs)
        
