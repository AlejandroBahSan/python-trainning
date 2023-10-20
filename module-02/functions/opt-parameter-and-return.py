"""
Optional paramete:
In Python, you can define optional parameters in a function by assigning default values to those parameters. 
When a function is called, if a value is not provided for an optional parameter, it will use its default value. 


Return: 
In Python, the return statement is used within a function to specify the value that the function will output when it is called or invoked. 
When a function reaches a return statement, it immediately exits, and the specified value is returned to the caller. 
The caller can then use this returned value in their code.
"""

# functions example (optional parameter & return) - 05


def calc(number_one, number_two, basic=False):

    add = number_one + number_two
    sub = number_one - number_two
    mul = number_one * number_two
    div = number_one / number_two

    string = ""

    string += "Addition: " + str(add)
    string += "\n"
    string += "Substraction: " + str(sub)
    string += "\n"
    string += "Multiplication: " + str(mul)
    string += "\n"
    if basic != True:
        string += "Division: " + str(div)
        string += "\n"
    return string


print(calc(10, 5, True))
