from commands.Command import Command

class CommandManager:
    def __init__(self, cmd_repo=[]):
        self.commands: dict = {}
        for cmd_cls in cmd_repo:
            self.register_command(cmd_cls)

    # command attr is a subclass of Command (cant find a way to type hint this)
    def register_command(self, command):
        self.commands[command.name] = command

    def execute_command(self, user_input: str):
        parts: list = user_input.split()
        if not parts:
            return "No command provided."

        command_name: str = parts[0]
        # args are the remaining parts of the input from index 1 to the end
        args: list = parts[1:]
        command = self.commands.get(command_name)

        if not command:
            return f"Command '{command_name}' not found."

        return command.execute(*args)
