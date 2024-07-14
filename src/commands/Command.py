class Command:
    def __init__(self, name):
        self.name = name

    def execute(self, *args):
        raise NotImplementedError("Implemnt execute method in subclass.")
