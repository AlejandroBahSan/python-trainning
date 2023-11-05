# sets and dictionaries - example 03


people_profiles = [
    {
        "name": "John Doe",
        "email": "johndoe@example.com",
        "phone": "123-456-7890",
        "address": "123 Main St, Anytown, USA"
    },
    {
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "phone": "098-765-4321",
        "address": "456 Elm St, Somecity, USA"
    },
    {
        "name": "Alice Johnson",
        "email": "alicej@example.com",
        "phone": "555-666-7777",
        "address": "789 Maple Dr, Thistown, USA"
    }
]

for profiles in people_profiles:
    print(
        f"The contact's name is: {profiles['name']} \nThe contact's email addres is: {profiles['email']} \nThe contact's phone addres is: {profiles['phone']} \n")
