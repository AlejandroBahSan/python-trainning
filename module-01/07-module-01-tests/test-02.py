"""
Module 01 - Test 02

## Instructions

* Develop a script that shows the even numbers from 1 to 121

* Show the even numbers using print()

"""


verification_number = 2

for counter in range (1, 121):
    if counter % verification_number == 0:
       print(f"The number {str(counter)} is an even number")
    # else:
    #     print(f"{counter} is not an even number")

    counter += 1