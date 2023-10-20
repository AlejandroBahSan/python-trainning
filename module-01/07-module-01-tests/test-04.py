"""
Module 01 - Test 04

## Instructions

* Develop a script that request & shows the basic math operations between the two numbers requested to the user.

* Show the result using print()

"""

first_users_number = int(input("Please input the first number: "))
second_users_number = int(input("Please input the second number: "))

subtraction = first_users_number - second_users_number
addition = first_users_number + second_users_number
multiplication = first_users_number * second_users_number
division = first_users_number / second_users_number

print(f"Great! Here are the results of the basic math operations between the numbers you chose, {first_users_number} and {second_users_number}")
print(f"\n The results of the substraction is {subtraction} \n The result of the addition is {addition} \n The result of the multiplicaction is {multiplication} \n The result of the division is {division}")