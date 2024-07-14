class Command:
    def __init__(self, name):
        self.name: str = name

    def execute(self, *args):
        raise NotImplementedError("Implement execute method in subclass.")
