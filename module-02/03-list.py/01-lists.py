"""
In Python, both lists and tuples are used to store collections of items. They are both sequence types and can contain items of any data type, including other lists or tuples. 
However, there are significant differences between them:

Mutability:

List: Lists are mutable, which means you can modify their content. You can add, remove, or modify items after the list is created.
"""

my_list = [1, 2, 3]
my_list[0] = 99  # Changing the first element
print(my_list)  # [99, 2, 3]

"""
Tuple: Tuples are immutable. Once a tuple is created, you can't alter its contents - meaning you can't add, delete, or modify items in a tuple.
"""
my_tuple = (1, 2, 3)
# my_tuple[0] = 99  # Uncommenting this line will raise an error

"""
Syntax:

List: Lists are defined by enclosing the items (elements) in square brackets [].
Tuple: Tuples are defined by enclosing the items in parentheses (). 
A tuple with a single item needs a trailing comma to differentiate it from a regular value in parentheses. 
For example, (5,) is a tuple containing a single item, while (5) is just the number 5.

Performance:
Since tuples are immutable, they generally have faster performance compared to lists when used as keys for dictionary operations or when being iterated over in loops.
Methods:

List: Lists provide a variety of methods such as append(), remove(), insert(), pop(), and more.
Tuple: Since tuples are immutable, they don't have methods like append() or remove(). However, common methods like index() and count() can be used.

Use Cases:
List: If you need a collection that might change in the future (e.g., adding or removing items), then lists are the more appropriate choice.
Tuple: If you have data that shouldn't change, then using a tuple can be a good way to ensure that it remains constant throughout the lifetime of a program. 
They're also commonly used as keys in dictionaries, where immutability is a requirement.

Memory Usage:
Tuples can be more memory efficient than lists because they don't have the extra overhead associated with the mutability features lists provide.
In summary, whether you should use a list or a tuple depends on the specific use case and whether you need mutability or immutability. 
Understanding the properties of each can help in deciding which one to use in different situations.
"""


# Lists example - 01

# Define lists
movies = ["Spiderman", "Advengers", "Lord of the rings"]
singers = list(("Adele", "Shakira", "Beyonce"))  # Converts a tuple into a list
years = list(range(2020, 2051))

print(movies, "\n", singers, "\n", years)

# Index of lists
print(movies[0])
print(singers[0:2])
movies[0] = "Stich"
print(movies)

# Append and Insert

# append(): Takes only one argument, which is the element you want to add.
singers.append("The Weeknd")
print(singers)
("""insert(): Takes two arguments. The first argument is the index at which the element needs to be inserted, and the second argument is the element you want to insert.""")
singers.insert(1, "Drake")
print(singers)
