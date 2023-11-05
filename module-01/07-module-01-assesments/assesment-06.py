"""
Module 01 - assesment 06

## Instructions

* Develop a script using operators where the multiplication tables from number one to number ten are shown, and each table with each number as a title

* Show the result using print()

"""
# Loop through numbers from 1 to 10
for first_factor in range(1, 11):
    # Print the title for the current table
    print("##############################################################")
    print(f"############ MULTIPLICATION TABLE FOR {first_factor} ###########")
    print("##############################################################")
    # Generate and print the multiplication table for the current number
    for second_factor in range(1, 11):
        print(f"{first_factor} x {second_factor} = {first_factor*second_factor}")
        # Add a newline for separation between tables
        print("\n")
