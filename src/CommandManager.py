class CommandManager:
    def __init__(self):
        self.commands = {}

    def register_command(self, command):
        self.commands[command.name] = command

    def execute_command(self, user_input):
        parts = user_input.split()
        if not parts:
            return "No command provided."

        command_name = parts[0]
        # args are the remaining parts of the input from index 1 to the end
        args = parts[1:]
        command = self.commands.get(command_name)

        if not command:
            return f"Command '{command_name}' not found."

        return command.execute(*args)
