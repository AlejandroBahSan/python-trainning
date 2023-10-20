"""
A function is a reusable block of code that performs a specific task or set of tasks. 
Functions are essential for structuring and organizing your code, promoting code reusability, and making your code more modular and easier to maintain.
"""


# functions example - 03

# function define
print("#### Example 3 ####")


def multiplication_table(number):
    print(f"Multiplication table of the number: {number}")

    for counter in range(11):
        math_operation = number * counter
        print(f"{number} x {counter} = {math_operation}")

    print("\n")


multiplication_table(3)

print("\n")

for number_multiplication_table in range(1, 11):
    multiplication_table(number_multiplication_table)
