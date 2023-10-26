"""
Global Variable:

A variable declared outside a function or in the global space is called a global variable.
It can be accessed from any function in the code, but to modify it inside a function, you typically need to use the global keyword.
Its scope is throughout the code, which means it can be accessed and modified from anywhere in the code (considering the correct usage of global keyword when necessary).
 _______________________________________________________________________________________________________________________________________________________________________
Local (or Normal) Variable:

A variable declared inside a function is called a local variable.
Its scope is limited to that function, which means it can be accessed and modified only inside the function where it is declared.
Once the function completes execution, the local variable is destroyed.

"""

# Local variables - Example 07


def phrase():
    phrase = ("Whimsical clouds drift above, capturing fleeting dreams"
              "while silent whispers echo amidst forgotten tales of enchanted twilight serenades")
    print(phrase)


print(phrase())


def phrase_two():
    # This tells Python we're referring to the global variable named phrase_two
    global global_phrase
    global_phrase = ("Whimsical clouds drift above, capturing fleeting dreams"
                     "while silent whispers echo amidst forgotten tales of enchanted twilight serenades")
    print("Locally", global_phrase)


phrase_two()
print("Globally", global_phrase)
"""
IMPORTANT TO REMEMBER: Overusing 'global variables' can make code harder to understand and maintain. 
It's often better to pass variables explicitly to functions or use class attributes to share state when needed.
"""
