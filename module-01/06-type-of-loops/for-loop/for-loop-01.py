# ************ FOR ************

""" the for statement is used to create a loop that iterates over a sequence (such as a list, tuple, string, or range) or other iterable objects. 
It allows you to execute a block of code repeatedly for each item in the sequence, until there are no more items left to process."""

print("\n ###### EXAMPLE 01 ######")

#Example-01
counter = 0
result = 0

for counter in range(0, 5):
    print("counting the number " + str(counter))
#using the += assigment operator which is the same as  result = result + counter
    result +=  counter

print(f"The result is: {result}")




