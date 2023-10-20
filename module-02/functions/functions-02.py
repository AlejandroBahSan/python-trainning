"""
A function is a reusable block of code that performs a specific task or set of tasks. 
Functions are essential for structuring and organizing your code, promoting code reusability, and making your code more modular and easier to maintain.
"""


# functions example - 02

# function define
print("#### Example 2 ####")

# Parameters


def whatIsYourNameAndAge(name, age):
    print(f" Hello there, {name}")
    if age >= 18:
        print("Great! You are old enough")


# Invocate the function
"""whatIsYourNameAndAge("This is - Alejandro")
whatIsYourNameAndAge("This is - Andres")
whatIsYourNameAndAge("This is - Ons")
"""
name = input("\nWhat is your name? ")
age = int(input("\nHow old are you? "))
whatIsYourNameAndAge(name, age)
