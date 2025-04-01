"""
Built-in Shell Commands Module

This module defines and executes built-in shell commands.
It provides implementations for commands like `exit`, `echo`, `type`, `pwd`, and `cd`.

Features:
- Defines a set of built-in commands supported by the shell.
- Implements functions for executing these commands.
- Integrates with `utils.py` for command type checking and directory changes.

Author: Neel Patel
"""
import os
import sys
from utils import check_command_type, change_directory  # Import utility functions

# Set of supported built-in commands
BUILTINS = {"exit", "echo", "type", "pwd", "cd"}

def execute_builtin(command_args):
    """
    Execute built-in shell commands.

    This function determines the built-in command to execute and calls the corresponding function.

    Supported commands:
    - `exit [status]`: Exits the shell with an optional exit status.
    - `echo [args]`: Prints the given arguments as a string.
    - `type [command]`: Checks if the given command is built-in or external.
    - `pwd`: Prints the current working directory.
    - `cd [directory]`: Changes the current directory.

    Args:
        command_args (list): List of command arguments, where `command_args[0]` is the command name.

    Returns:
        tuple: (error_message, output_message) - Error messages for invalid inputs, or output messages.
    """

    command = command_args[0]

    # Exit the shell with an optional status code
    if command == "exit":
        sys.exit(int(command_args[1]) if len(command_args) > 1 else 0)

    # Print the given arguments as a single string
    elif command == "echo":
        return "", " ".join(command_args[1:])

    # Check if the given command is built-in or external
    elif command == "type":
        if len(command_args) < 2:
            return "type: missing operand", ""
        return "", check_command_type(command_args[1])

    # Print the current working directory
    elif command == "pwd":
        return "", os.getcwd()

    # Change the current directory
    elif command == "cd":
        if len(command_args) < 2:
            return "cd: missing argument", ""
        return "", change_directory(command_args[1])

    # Return empty strings if no valid built-in command is found
    return "", ""
