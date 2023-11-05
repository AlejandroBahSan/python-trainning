"""
A set is an unordered collection of unique elements. 
Sets are mutable, but the elements contained must be of immutable types (e.g., numbers, strings, tuples).

Characteristics:
Unordered: The items have no index.
No duplicate members.
Elements in the set are immutable, but the set itself is mutable, meaning we can add or remove items from it.
"""

# sets and dictories - example 01

names = {
    "Victor"
    "Manuel"
    "Frank"
}

names.add("Patric")
names.remove("Frank")

print(type(names))
print(names)
