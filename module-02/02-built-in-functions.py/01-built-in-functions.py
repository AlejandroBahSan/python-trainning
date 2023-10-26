"""
For a comprehensive list and their details, you can refer to: https://docs.python.org/3/library/functions.html
Python provides a rich set of built-in functions that are always available for use. 
These functions perform a wide range of operations and are a fundamental part of the language. 
"""

name = "Alejandro Bahena"
# Basic Functions
print(name)  # Outputs arguments to the console.
print(type(name))  # Returns the type of an object.
# ____________________________________________________________________________________
text = "        ff  "
if len(text) <= 0:
    print("The variable is empty")
else:
    print("The variable has a lenght of:", len(
        text), "Characters, this number is counting every single character, even the blank spaces")

# Attributes and Introspection
# isinstance: Checks if an object is an instance of a specified type or class tuple.
check = isinstance(name, str)
if check:
    print(f"The variable is a string")

if not isinstance(name, float):
    print("The variable is not a float number")
# ___________________________________________________________________________________
phrase = "       This is my content"
print(phrase)
# Without any argument will remove leading and trailing whitespaces
print(phrase.strip())


"""
For future reference - Commonly used built-in functions.

Basic Functions:

print(): Outputs arguments to the console.
input(): Reads a line from input and returns it as a string.
len(): Returns the length of an object.
type(): Returns the type of an object.

Numeric Functions:

abs(): Returns the absolute value of a number.
max(): Returns the largest of the provided arguments.
min(): Returns the smallest of the provided arguments.
pow(): Raises a number to a power.
round(): Rounds a number.

Type Conversion:

int(): Converts a value to an integer.
float(): Converts a value to a floating-point number.
str(): Converts a value to a string.
bool(): Converts a value to a boolean.

Data Structure Functions:

list(): Converts a value to a list.
tuple(): Converts a value to a tuple.
set(): Converts a value to a set.
dict(): Creates a new dictionary.
sorted(): Returns a sorted list from the specified iterable.

Character and String Functions:

chr(): Returns a string representing a character whose Unicode code is the integer argument.
ord(): Returns an integer representing the Unicode character.
format(): Formats a specified value.

Miscellaneous:

enumerate(): Returns an enumerate object.
range(): Generates a sequence of numbers.
reversed(): Returns a reversed iterator.
zip(): Combines multiple iterables into tuples.

File and I/O:

open(): Opens a file and returns a file object.

Attributes and Introspection:

getattr(): Returns the value of a named attribute of an object.
hasattr(): Determines if an object has a given attribute.
setattr(): Sets the value of a named attribute.
dir(): Returns a list of valid attributes for the given object.
isinstance(): Checks if an object is an instance of a specified type or class tuple.
issubclass(): Checks if a class is a subclass of a specified class or class tuple.

Other Important Functions:

eval(): Evaluates a string as Python code.
exec(): Executes a string as Python code.
globals(): Returns the dictionary of the current global symbol table.
locals(): Returns the dictionary of the current local symbol table.
"""
