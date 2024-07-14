from commands.Command import Command

class HelpCommand(Command):
    def execute(self, *args: str) -> str:
        return f"Avaiable commands: help, greet <greeting> <name>, add <num1> <num2>, exit"
