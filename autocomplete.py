"""
Shell Command Auto-Completion Module

This module provides auto-completion functionality for the custom shell.
It enables users to quickly complete built-in commands by pressing the Tab key.

Features:
- Uses Python's `readline` library for auto-completion.
- Provides suggestions based on available built-in commands.
- Filters commands based on user input.

Author: Neel Patel
"""

from builtin_commands import BUILTINS   # Import built-in command set

def auto_completer(text, state):
    """
    Auto-completes built-in shell commands.

    This function is used as a completer for Python's `readline` module.
    When a user types part of a command and presses Tab, it suggests
    matching built-in commands.

    Args:
        text (str): The current user input for command completion.
        state (int): The index of the completion candidate.

    Returns:
        str or None: The matched command at the given state index, or None if there are no more matches.
    """

    # Split the input text into components based on spaces
    # This helps support auto-completing partial commands in multi-word inputs
    components = text.split(" ")

    # Filter built-in commands that start with the first word of the input
    builtin = [command for command in BUILTINS if command.startswith(components[0])]

    # Return the corresponding match based on the state index
    if state < len(builtin):
        # Append the rest of the typed text after the auto-completed command
        return builtin[state] + " " + " ".join(components[1:])

    # If no match is found and it's the first state request, trigger an alert sound (bell)
    elif state == 0:
        print("\a", end="", flush=True)

    # Return None if no matches are available
    else:
        return None
