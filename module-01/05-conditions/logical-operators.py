#Logical operators - multiple conditions 

"""1. Logical AND (and):
The and operator returns True if both operands are True.

Example"""
x = True
y = False
result = x and y  # result will be False because both x and y are not True


"""
2. Logical OR (or):
The or operator returns True if at least one of the operands is True.

Example:
"""
x = True
y = False
result = x or y  # result will be True because x is True (even though y is not)




"""
3. Logical NOT (not):
The not operator negates a Boolean value. If the operand is True, not makes it False, and vice versa.

Example:
"""
x = True
result = not x  # result will be False because not True is False



#Example 01 - multiple conditions
print("""\n******** EXAMPLE 01 ********""")

labor_old = int(input("How long have you been working in this company?: "))
income = int(input("What is your current salary?: "))

if labor_old >= 1 and income >= 3000:
    print("Congratulations! You qualify for the loan")
else:
    print("I'm sorry, you do not qualify for the loan")    