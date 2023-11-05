"""
Module 01 - assesment 08

## Instructions

* Develop a script that requests the user a number and what percentage would the user like to devide it for.
* Show the result using print()

"""

users_number = int(input("Please input the first number: "))
percentage = int(input(
    f"Please input the percentage that you'd like to get from the {users_number}: %"))

user_number_percentage = float(users_number * percentage / 100)

print(f"The {percentage}% of the number {users_number} is {user_number_percentage}")
