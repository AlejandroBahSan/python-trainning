#Example - 02

print("\n ###### EXAMPLE 02 -WHILE LOOP ######")

users_number = int(input("What number would you like to do the multiplication table for? "))

if users_number < 1:
    users_number

print(f"\n ### The multiplication table for the number {users_number} is ###")

counter = 1
while counter <= 10:
    print(f"\n {users_number} x {counter} = {users_number*counter}")
    counter += 1

else: 
    print(f"\n ### Math operation done. ###")