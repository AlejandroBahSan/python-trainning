"""
In Python, a variable is a named container or storage location that holds data or values, such as numbers, strings, lists, or more complex objects. 
Variables are used to store and manipulate data in a program. You can think of variables as labels or identifiers that reference a specific memory location where the data is stored.

Here's how you declare and use a variable in Python:

1. **Variable Declaration**:
   To declare a variable, you simply provide a name for it and assign a value to it using the assignment operator (`=`). You don't need to specify the data type explicitly because Python is dynamically typed, meaning it determines the data type automatically based on the assigned value.

   ```python
   variable_name = value
   ```

   For example:
   ```python
   age = 30
   name = "John"
   ```

2. **Variable Names**:
   Variable names in Python must follow certain rules:
   - They can contain letters (a-z, A-Z), digits (0-9), and underscores (_).
   - They cannot start with a digit.
   - Variable names are case-sensitive (e.g., `myVar` and `myvar` are different variables).
   - Python has reserved keywords (e.g., `if`, `for`, `while`, etc.) that cannot be used as variable names.

3. **Data Types**:
   Variables can hold various data types, such as:
   - **int**: Integer numbers (e.g., `age = 30`).
   - **float**: Floating-point numbers (e.g., `price = 19.99`).
   - **str**: Strings (e.g., `name = "John"`).
   - **list**: Ordered collections of items (e.g., `fruits = ["apple", "banana", "cherry"]`).
   - **dict**: Key-value pairs (e.g., `person = {"name": "John", "age": 30}`).
   - **bool**: Boolean values (`True` or `False`) (e.g., `is_adult = True`).

4. **Reassigning Variables**:
   You can change the value of a variable by assigning it a new value:

   ```python
   age = 30
   age = 31  # Reassigning the variable 'age'
   ```

Variables are fundamental in Python programming as they allow you to store, manipulate, and access data throughout your code. 
Depending on the scope and usage, variables can have different lifetimes and visibility within a program. Understanding how to use variables effectively is essential for writing Python programs.
"""

text = "Python master"
number = 31
float = 31.29
dict = ({"Lex":31, "Ons":29, "Sas":1})

print(text)
print(number, float, dict)

#concatenate 

name = "Alejandro"
last_name = "Bahena"
full_last_name = (f"{last_name}" " Sandoval")
website = "https://alejandro-bs.ca"

print(name + " " + last_name + " - " + website)
#f"{}" concatenates the value of each variable 
print(f"{name} {full_last_name} - {website}")

print("Hi there, my name is {} {} and my website is: {}".format(name, full_last_name, website))