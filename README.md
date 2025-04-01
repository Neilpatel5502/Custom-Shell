# Custom Shell in Python

## Introduction

A shell is a command-line interface that executes commands and manages processes. In this challenge, I built my own POSIX compliant shell that is capable of interpreting shell commands, running external programs, and implementing built-in commands like `cd`, `pwd`, `echo`, `type`, and more. This project helped me understand shell command parsing, REPLs, built-in commands, and more.

## Features

### 1. **Command Parsing and REPL Loop**
   - A custom Read-Eval-Print-Loop (REPL) was built to handle user inputs and execute commands continuously until the user exits the shell.
   - The shell interprets and processes both built-in and external commands.

### 2. **Built-in Commands Support**
   I implemented several built-in commands that are fundamental to shell behavior:
   - `exit`: Exits the shell, optionally with a specific status code.
   - `echo`: Prints arguments to the terminal.
   - `pwd`: Displays the current working directory.
   - `cd`: Changes the current working directory.
   - `type`: Displays information about the command type (whether it is a built-in command or external executable). (`type: built-in command`)

### 3. **External Command Execution**
   - The shell can execute external commands by calling system programs using the `subprocess` module. The shell can handle command execution with proper error handling for non-existent commands.
   - Supports both stdout and stderr output redirection.

### 4. **Redirection Handling**
   - Implemented output redirection using the `>` and `>>` operators.
   - The shell can redirect output to a file, either overwriting the file with `>` or appending to it with `>>`.

### 5. **Auto-completion**
   - Added an auto-completion feature for built-in shell commands using Python’s `readline` library. This allows the user to complete commands by pressing the Tab key.

### 6. **Quoting and Escape Handling**
   - Implemented robust support for quoting mechanisms, including single quotes (`'`), double quotes (`"`), and backslashes (`\`).
   - Single quotes preserve the literal value of characters inside them.
   - Double quotes preserve characters except for special ones like backslashes, dollar signs, and double quotes.
   - Backslashes escape characters and preserve their literal values, with special handling within quotes.

## Challenges Faced

### 1. **Command Parsing**
   - Developing an efficient parser for shell commands that could handle both arguments and redirection operators was challenging. The shell needed to properly identify and parse input to execute commands correctly.

### 2. **Built-in Command Implementation**
   - Implementing commands like `cd`, `echo`, `pwd`, and `exit` required careful handling of system resources, such as the current working directory and managing the state of the shell.

### 3. **External Command Execution**
   - Handling external commands involved ensuring the shell could run system programs while capturing both their standard output and error messages. I used Python's `subprocess` module to achieve this.

### 4. **Redirection Syntax**
   - Supporting redirection operators like `>`, `>>`, and `2>` required me to adjust how the shell handles output and errors, determining when to redirect output to a file instead of printing it to the terminal.

### 5. **Quoting and Escaping**
   - Implementing proper parsing of quoted strings, including handling single and double quotes as well as backslashes, required careful attention to edge cases and string manipulation.

### 6. **Auto-completion**
   - Implementing auto-completion for built-in commands required using the `readline` library, which was a key addition for improving the user experience.

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
2. Run the main.py file:
   ```bash
   python main.py
