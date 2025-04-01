"""
Redirection Handler Module

This module handles output redirection for shell commands.
It checks for output redirection operators (e.g., `>`, `>>`, `1>`, `1>>`, `2>`, `2>>`),
and extracts the necessary information to apply redirection to the output of a command.

Features:
- Identifies redirection operators in a command.
- Extracts the file name and redirection type (write or append).
- Handles redirection to standard output or error.
- Provides error handling for missing file names.

Author: Neel Patel
"""

def handle_redirection(command_args):
    """
    Extracts redirection information from the command arguments.

    This function checks if the command includes redirection operators (such as `>`, `>>`, `1>`, `1>>`, `2>`, `2>>`).
    If any redirection operator is found, it extracts the associated output file and specifies whether to append
    or overwrite the file. It also handles the case where the file name is not provided after the redirection operator.

    Args:
        command_args (list of str): The command arguments passed by the user, which may include redirection operators.

    Returns:
        tuple: A tuple containing:
            - command_args (list of str): The command arguments without the redirection operator.
            - output_file (str or None): The output file name, or None if no redirection.
            - redirect (bool): Whether redirection was found.
            - second_red (bool): Whether the redirection is for standard error (`2>`).
            - operation_type (str or None): The type of redirection (`write` or `append`), or None if no redirection.
    """

    # Initialize flags and variables to store redirection information
    redirect = False
    output_file = None
    second_red = False
    operation_type = None

    # Define the possible redirection operators and their corresponding actions
    redirection = {
        "1>>": "append", "2>>": "append", ">>": "append",   # Append redirection
        "1>": "write", "2>": "write", ">": "write",         # Overwrite redirection
    }

    # Loop through the redirection operators to check if any are present in the command
    for redir, operation in redirection.items():
        if redir in command_args:
            try:
                # Find the index of the redirection operator in the command
                redir_index = command_args.index(redir)

                # The next argument should be the output file
                output_file = command_args[redir_index + 1]

                # Remove the redirection part from the command arguments
                command_args = command_args[:redir_index]

                # Set the redirection flag and operation type
                redirect = True
                operation_type = operation

                # If the redirection is for standard error (e.g., "2>"), set the second_red flag
                if "2" in redir:
                    second_red = True

                # Exit the loop once redirection is found
                break
            except IndexError:
                # Handle the case where the redirection operator is missing the file name
                print("Syntax error: No output file specified")
                return command_args, None, False, False, None

    # Return the updated command arguments along with the redirection details
    return command_args, output_file, redirect, second_red, operation_type
