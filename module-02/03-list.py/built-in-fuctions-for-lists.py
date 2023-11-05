
# Lists - Example-04


singers = ["Adele", "Ed Sheeran",
           "Billie Eilish", "Bruno Mars", "Taylor Swift"]
numbers = [102, 2, 3, 30, 10, 75]

# sort
print(numbers)
numbers.sort()
print(numbers)

# append / insert
singers.append("The Weeknd")
print(singers)
singers.insert(1, "Bad Bunny")
print(singers)


# delete / pop an element / remove
singers.pop(2)
print(singers)
singers.remove("Bad Bunny")
print(singers)


# reverse
numbers.reverse()
print(numbers)

# search in list
print("Taylor Swift" in singers)
print(singers.index("Taylor Swift"))

# number of elements in a list.
print(len(singers))

# element times in a list.
numbers.append(102)
print(numbers.count(102))

# join lists
singers.extend(numbers)
