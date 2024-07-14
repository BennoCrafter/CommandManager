from CommandManager import CommandManager
from commands.AddCommand import AddCommand
from commands.GreetCommand import GreetCommand
from commands.HelpCommand import HelpCommand


if __name__ == "__main__":
    manager = CommandManager()

    manager.register_command(GreetCommand(name="greet"))
    manager.register_command(AddCommand(name="add"))
    manager.register_command(HelpCommand(name="help"))

    while True:
        user_input: str = input("Enter command: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        result = manager.execute_command(user_input)
        print(result)
