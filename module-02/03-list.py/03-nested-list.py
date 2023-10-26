"""
A multi-dimensional list, often called a nested list, is a list where each item can be a list itself. 
The most common use case is a 2-dimensional list (similar to a table or matrix), but you can have lists with more dimensions if required.
"""

# Lists - Example-03


contact_info = [

    [
        "John",
        "John@email.com"
    ],
    [
        "Fredd",
        "Fredd@email.com"
    ],

    [
        "Dann",
        "Dann@email.com"
    ],
    [
        "Edd",
        "Edd@email.com"
    ]
]

for contacts in contact_info:
    for el in contacts:
        if contacts.index(el) == 0:
            print("Name: " + el)
        else:
            print("Email: " + el)
    print("\n")
