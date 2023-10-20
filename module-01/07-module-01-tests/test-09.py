"""
Module 01 - Test 09

## Instructions

* Develop a script that requests the user numbers indefinitely until the user inputs the number 111.
* Show the result using print()

"""

number_requested = int(input("Please input the any number: "))


while number_requested != 111:
    number_requested = int(input("Please input the any number: "))
