from commands.Command import Command

class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            return "Invalid input. Usage: add <num1> <num2>"
        try:
            a = int(args[0])
            b = int(args[1])
            return a + b
        except ValueError:
            return "Invalid numbers provided. Usage: add <num1> <num2>"
