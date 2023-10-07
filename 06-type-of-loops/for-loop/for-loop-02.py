
#Example-02

print("\n###### EXAMPLE 02 - Multiplication table ######")

users_number = int(input("What number would you like to do the multiplication table for? "))


if users_number < 1:
    users_number = 1
print(f"The multiplication table for the number {users_number} is")

for times_users_number in range (1, 11):
    if users_number == 45:
        print("Only numbers from 1 - 10 allowed")
        break
    print(f"{users_number} x {times_users_number} = {users_number*times_users_number}")
else:
    print("The math operation is done")    