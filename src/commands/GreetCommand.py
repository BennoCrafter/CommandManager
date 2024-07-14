from commands.Command import Command

class GreetCommand(Command):
    def execute(self, *args: str) -> str:
        if len(args) != 2:
            return "Invalid input. Usage: greet <greeting> <name>"

        greeting, name = args[0], args[1]
        return f"{greeting}, {name}!"
