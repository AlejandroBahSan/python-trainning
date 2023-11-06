# File System in Python Guide

This guide provides an overview of how to interact with the file system in Python. Python's built-in modules like `os`, `os.path`, and `shutil` offer a range of functionalities for file system operations.

## Overview of File System Operations

Python allows you to handle files and directories through its standard library, enabling you to create, read, update, and delete files or directories on your operating system.

## Working with Files

### Opening a File

To open a file, you can use the built-in `open()` function, which returns a file object:

```python
file = open('example.txt', 'r')  # Opens a file for reading ('r')
Reading from a File
Once a file is opened, you can read from it in several ways:

python
Copy code
content = file.read()       # Read the entire file
line = file.readline()      # Read the next line
lines = file.readlines()    # Read all the lines into a list
Writing to a File
To write to a file, you must open it in write ('w') or append ('a') mode and then call the file object's write method:

python
Copy code
file = open('example.txt', 'w')  # Opens a file for writing ('w')
file.write('Hello, Python!')
Closing a File
It is important to close the file when you're done with it:

python
Copy code
file.close()
Using with Statements
The with statement provides a way to ensure that a file is closed when the block inside the with statement is exited:

python
Copy code
with open('example.txt', 'r') as file:
    content = file.read()
Working with Directories
Navigating the File System
You can use the os module to navigate and manipulate the file system:

python
Copy code
import os

current_dir = os.getcwd()  # Get the current working directory
os.chdir('/path/to/dir')   # Change the current working directory
os.listdir('.')            # List all files and directories in the given directory
Creating and Deleting Directories
The os module can also be used to create and remove directories:

python
Copy code
os.mkdir('new_directory')         # Create a new directory
os.rmdir('new_directory')         # Remove a directory
Copying and Moving Files
The shutil module offers high-level operations on files and collections of files:

python
Copy code
import shutil

shutil.copy('source.txt', 'dest.txt')    # Copy a file
shutil.move('source.txt', 'dest.txt')    # Move a file
Resources
Python's Official Documentation for the os module: https://docs.python.org/3/library/os.html
Python's Official Documentation for the shutil module: https://docs.python.org/3/library/shutil.html
Real Python - Working With Files in Python: https://realpython.com/working-with-files-in-python/
GeeksforGeeks - File Handling in Python: https://www.geeksforgeeks.org/file-handling-python/
Contributions
Contributions to this guide are welcome! If you have additional examples, best practices, or tips on Python file system operations, please feel free to share.

License
This guide is provided under the MIT License.