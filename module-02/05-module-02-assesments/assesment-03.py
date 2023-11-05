"""Write a program that checks if a variable is empty and if it is empty, fill it with lowercase text and display it in uppercase"""


# Initialize a variable. We'll start with it being empty.
text = "        "

# Check if the variable is empty
if text.strip() == "":  # strip() method to remove blank spaces
    # Since it's empty, we fill it with some lowercase text.
    text = "this is some lowercase text"

    # Now we display that text in uppercase.
    print(text.upper())
else:
    print(f"The variable text is not empty, here's what it has {text.strip()}")
