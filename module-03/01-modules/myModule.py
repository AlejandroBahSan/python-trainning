"""
Calculator module
"""


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
