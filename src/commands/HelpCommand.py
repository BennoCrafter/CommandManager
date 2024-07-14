from commands.Command import Command

class HelpCommand(Command):
    def execute(self, *args: str) -> str:
        return f"Avaiable commands:\n help\n greet <greeting> <name>\n add <num1> <num2>\n exit"
