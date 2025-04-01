"""
Utility Functions Module

This module contains utility functions for the shell application.
It provides helpers for checking command types and changing directories.

Features:
- Checks if a command is a built-in shell command or an external executable.
- Provides a function to change the working directory and handle common errors.

Author: Neel Patel
"""

import os
import shutil

def check_command_type(cmd):
    """
    Check if a command is built-in or an external executable.

    This function checks whether the provided command is one of the built-in shell commands
    or if it corresponds to an external executable available in the system's PATH.

    Args:
        cmd (str): The command to check (e.g., "echo", "pwd", "ls").

    Returns:
        str: A message indicating whether the command is a built-in or an external executable,
             or if it is not found.
    """

    # Check if the command is a built-in shell command
    if cmd in {"exit", "echo", "type", "pwd", "cd"}:
        return f"{cmd} is a shell builtin"

    # Otherwise, check if it is an external executable available in the system's PATH
    return f"{cmd} is {shutil.which(cmd) or 'not found'}"

def change_directory(path):
    """
    Change the working directory.

    This function attempts to change the current working directory to the specified path.
    It handles errors that may arise when the path is invalid, not a directory, or permission is denied.

    Args:
        path (str): The path to change the directory to (could be relative or absolute).

    Returns:
        str: An error message if the directory change fails, otherwise an empty string on success.
    """

    try:
        # Attempt to change the directory, expanding user directories (e.g., ~)
        os.chdir(os.path.expanduser(path))
        return ""   # Return an empty string on success

    except FileNotFoundError:
        # Error case where the path does not exist
        return f"cd: {path}: No such file or directory"

    except NotADirectoryError:
        # Error case where the path exists but is not a directory
        return f"cd: {path}: Not a directory"

    except PermissionError:
        # Error case where permission is denied to access the path
        return f"cd: {path}: Permission denied"
