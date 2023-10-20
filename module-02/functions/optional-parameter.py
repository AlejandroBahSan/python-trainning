"""
In Python, you can define optional parameters in a function by assigning default values to those parameters. 
When a function is called, if a value is not provided for an optional parameter, it will use its default value. 

"""

# functions example (optional parameter) - 04


def get_employee(name, id=None):
    print("Employee")
    print(f"Name: {name}")
    if id != None:
        print(f"ID: {id}")


get_employee("Alejandro")
