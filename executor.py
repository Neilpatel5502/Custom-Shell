"""
Command Execution Module

This module handles the execution of both built-in and external commands for the custom shell.
It also manages command redirection, ensuring output is written to files when necessary.

Features:
- Executes built-in commands by delegating to `execute_builtin()`.
- Executes external system commands using `subprocess`.
- Handles output redirection (`>`, `>>`, `2>`, `2>>`).
- Prints command output to the terminal unless redirected.

Author: Neel Patel
"""

import shutil
import subprocess
import shlex
from builtin_commands import BUILTINS, execute_builtin  # Import built-in command handling
from redirection import handle_redirection  # Import redirection handling

def execute_command(command):
    """
    Execute the given command, determining whether it is built-in or external.

    This function:
    - Parses the command string into arguments.
    - Checks for redirection (`>`, `>>`, `2>`, `2>>`) and handles it accordingly.
    - Executes built-in commands using `execute_builtin()`.
    - Executes external system commands if not built-in.
    - Handles output redirection, appending or overwriting files as specified.

    Args:
        command (str): The command string input by the user.

    Returns:
        None
    """

    # Split the command string into arguments while handling quoted strings correctly
    command_args = shlex.split(command)

    # Check for redirection and extract file handling details
    command_args, output_file, redirect, second_red, redirection_type = handle_redirection(command_args)

    # Determine whether the command is built-in or an external executable
    if command_args[0] in BUILTINS:
        error, output = execute_builtin(command_args)
    else:
        error, output = execute_external(command_args)

    # Handle output redirection if applicable
    if redirect and output_file:
        with open(output_file, "a" if redirection_type == "append" else "w") as f:
            # Ensure a newline if appending to an existing file
            if f.tell() > 1:
                f.write("\n")

            # Redirect error output (for `2>` or `2>>` redirection)
            if second_red:
                f.write(error)
                error = ""      # Prevents error from being printed to the terminal
            else:
                f.write(output)
                output = ""     # Prevents output from being printed to the terminal

    # Print any remaining error or output to the terminal
    if error:
        print(error.strip())
    if output:
        print(output.strip())

def execute_external(command_args):
    """
    Execute external system commands using `subprocess.run()`.

    This function:
    - Checks if the command exists using `shutil.which()`.
    - Runs the command using `subprocess.run()`, capturing standard output and error.
    - Returns both stdout and stderr as strings.

    Args:
        command_args (list): A list containing the command and its arguments.

    Returns:
        tuple: (error_message, output_message)
    """
    command = command_args[0]

    # Check if the command exists in the system's PATH
    if shutil.which(command):
        # Run the command, capturing stdout and stderr
        result = subprocess.run(command_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Return the error and output as trimmed strings
        return result.stderr.strip(), result.stdout.strip()

    # If the command is not found, return an appropriate error message
    return f"{command}: command not found", ""
