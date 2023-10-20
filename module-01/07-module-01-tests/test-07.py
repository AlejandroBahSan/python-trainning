"""
Module 01 - Test 07

## Instructions

* Develop a script that requests two numbers to the user and shows the odd numbers between them.
* Show the result using print()

"""

first_users_number = int(input("Please input the first number: "))
second_users_number = int(input("Please input the second number: "))
verification_number = 2

for counter in range(first_users_number, (second_users_number + 1)):
    if counter % verification_number != 0:
        print(f"The number {str(counter)} is an odd number")
