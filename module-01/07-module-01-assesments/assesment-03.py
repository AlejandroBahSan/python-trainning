"""
Module 01 - assesment 03

## Instructions

* Develop a script that shows the exponentiation of the first 60 natural numbers using the while and for loop

* Show the result using print()

"""

# While loop
while_loop_counter = 0

while while_loop_counter <= 60:
    while_number_exponentiation = while_loop_counter*while_loop_counter
    print(
        f"The exponentiation of the number {while_loop_counter} is {while_number_exponentiation}")
    while_loop_counter += 1


# For loop
for for_loop_counter in range(1, 61):
    for_number_exponentiation = for_loop_counter*for_loop_counter
    print(
        f"The exponentation of the number {for_loop_counter} is {for_number_exponentiation}")
