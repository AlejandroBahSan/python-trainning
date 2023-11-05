"""
Write a program that has four variables: a list, a string, an integer, and a boolean, 
and show what type of data each variable is, using functions.
"""


# Define the four variables
a_list = [1, 2, 3]      # This is a a_list
string = "Hello"       # This is a string
integer = 42          # This is an integer
boolean = True         # This is a boolean

# Define a function to print the type of a variable


def print_type(variable):
    if type(variable) == bool:
        print(f"The variable is a boolean")
    elif type(variable) == list:
        print(f"The variable is a list")
    elif type(variable) == str:
        print(f"The variable is a string")
    elif type(variable) == int:
        print(f"The variable is a integer")


# Use the function to print the type of each variable
print_type(a_list)
print_type(string)
print_type(integer)
print_type(boolean)
