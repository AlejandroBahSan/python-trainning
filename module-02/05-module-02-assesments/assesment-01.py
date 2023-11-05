"""
Exercise 1. Create a program that has a list of 8 integers and has the following function:

Traverse the list and display it
Sort and display it
Display its length
Search for an element (that the user requests through an input)
"""

# display the list of numbers


def display_list(nums):
    print("List:", nums)

# display the list of numbers but already sorted


def sort_and_display(nums):
    nums.sort()
    print("Sorted list:", nums)

# display the lists length


def display_length(nums):
    print("Length of the list:", len(nums))


def search_element(nums):
    el = int(input("Enter the integer you want to search for: "))
    if el in nums:
        print(f"{el} is in the list.")
    else:
        print(f"{el} is not in the list.")


def main():
    numbers = [23, 11, 89, 4, 56, 78, 15, 43]

    display_list(numbers)
    sort_and_display(numbers)
    display_length(numbers)
    search_element(numbers)


print(main())
