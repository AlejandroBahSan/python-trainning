"""
Module 01 - Test 05

## Instructions

* Develop a script that requests the user two random numbers, where the second number has to be greater than the first number, 
and the numbers between the range of numbers is shown

* Show the result using print()

"""


first_users_number = int(input("Please input the first number: "))
second_users_number = int(input("Please input the second number: "))

if first_users_number < second_users_number:
    for number_to_show in range (first_users_number, (second_users_number + 1)):
     print(number_to_show)
else:
    print("Please note that, the first number has to be less than the second number")