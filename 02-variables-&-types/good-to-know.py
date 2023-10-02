""" Specitial function - The backslash is an escape character in Python, and when it appears twice ("\"), it is used to escape the following character.
    For example, if you want to include a backslash in a string, you can use "\" to indicate that the second backslash is a literal 
    character and not an escape character:"""

my_string = "This is a backslash: \\"
print(my_string)

#More examples

text = '"Python"'
text2 = "\"Master\""

"""In Python, "\n" represents an escape sequence that is used to insert a newline character into a string. 
The newline character is a control character that signifies the end of a line of text and causes the text following it to be displayed on a new line. 
This is commonly used for formatting text and creating line breaks within strings."""
joined_text = text + "\n" + text2
print(joined_text)

"""
In Python, "\t" represents an escape sequence that is used to insert a horizontal tab character into a string. 
The horizontal tab character, often referred to as a "tab," is a control character that is used to advance the cursor to the next tab stop, typically at regular intervals. """
joined_text = text + "\t" + text2
print(joined_text)


"""
In Python, "\r" represents an escape sequence that is used to insert a carriage return character into a string. 
The carriage return character, often denoted as "\r," is a control character that causes the cursor or text input to move to the beginning of the current line without advancing to the next line. 
It's used to simulate going back to the start of a line, which can be useful in certain situations."""
joined_text = text + "\r" + text2
print(joined_text)
