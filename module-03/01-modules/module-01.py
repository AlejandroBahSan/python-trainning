# The entire module myModule is imported. This means you can access functions, classes, variables, etc., defined in myModule using the dot notation (myModule.itemName).
import myModule
# To import only the an specific object function, a class, or a variable that is defined within myModule.py.
from myModule import calc
from myModule import *
"""
"from myModule import *" imports all public objects, such as functions, classes, and variables, defined in the module named myModule into the current namespace. 
However, using from ... import * is generally discouraged because it can lead to confusion about which names are present in the current namespace, making the code harder to read and debug
"""

print(myModule.calc(1, 2, True))
print(calc(3, 5, True))
