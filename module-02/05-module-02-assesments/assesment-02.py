"""
Write a program that adds values to a list as long as its length is less than 120, and then display the list..
Plus: Use while and for loop
"""

# Initialize an empty list
numbers_list = []

# Continue to add values to the list as long as its length is less than 120
while len(numbers_list) < 120:
    # Here we'll simply add the next integer to the list
    # The value added is the current length of the list + 1
    numbers_list.append(len(numbers_list) + 1)

# Once the list has 120 elements, we'll display the list
# Printing the whole list at once
print(numbers_list)
# Using for loop
print("\nFor loop")
for number in numbers_list:

    print(number, end=", ")
