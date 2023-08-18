Simple File System Program
This is a simple Python program that simulates a basic file system. It provides a command-line interface to perform file and directory operations within the virtual file system.

Features:

Create files
Create directories
List contents of the current directory
Change the current directory
Exit the program

Usage
Run the program using Python:


python file_system.py


You will start in the root directory (/). The program prompt will show the current directory.

Available commands:

touch file_name: Create a new file with the given name in the current directory
mkdir dir_name: Create a new directory with the given name in the current directory
ls: List the contents of the current directory
cd path: Change the current directory to the specified path
exit: Exit the program
When using the touch or mkdir commands, you can provide paths relative to the current directory

For example:

touch file.txt creates a file named "file.txt" in the current directory.
mkdir my_folder creates a directory named "my_folder" in the current directory.
To navigate through directories, use the cd command followed by the path. You can use absolute paths to navigate.

The program will continue to run until you enter the exit command.
