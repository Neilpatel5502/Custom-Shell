"""
Custom Shell - Entry Point

This module serves as the entry point for the custom shell application. It sets up
command-line input handling, including auto-completion, and continuously listens for
user input to execute commands.

Features:
- Reads user input with a `$ ` prompt.
- Supports auto-completion for built-in commands.
- Gracefully handles exit signals (`Ctrl+C`, `Ctrl+D`).
- Passes valid commands to `execute_command()` for execution.

Author: Neel Patel
"""
import readline
from executor import execute_command    # Handles command execution logic
from autocomplete import auto_completer     # Provides command auto-completion

def main():
    """
    Main loop to run the custom shell.

    This function initializes the shell, sets up auto-completion, and continuously
    prompts the user for input. Commands entered by the user are processed and executed.

    The loop runs until the user exits manually using `Ctrl+D` (EOF) or `Ctrl+C` (KeyboardInterrupt).
    """

    # Configure readline for auto-completion
    readline.set_completer(auto_completer)
    readline.parse_and_bind("tab: complete")    # Enables tab-based command completion

    while True:
        try:
            # Display the shell prompt and capture user input
            command = input("$ ").strip()

            if command:
                execute_command(command)    # Process and execute the command

        except (EOFError, KeyboardInterrupt):
            # Gracefully handle user exit (`Ctrl+D` for EOF, `Ctrl+C` for interrupt)
            print("\nExiting shell.")
            break   # Exit the loop and terminate the shell process

if __name__ == "__main__":
    main()  # Run the shell when this script is executed directly
