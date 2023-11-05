
""""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


# Define a class called 'Solution'. In Python, a class is like a blueprint for creating objects.


class Solution:
    # This is a method of the class 'Solution'. It's like a function that belongs to the class.
    def removeDuplicates(self, nums):
        # Check if the list 'nums' is empty. If it is, return 0 because there are no elements to remove.
        if not nums:
            return 0

        # Initialize a variable to keep track of the position of the last unique element found.
        last_unique = 0

        # Start a loop from the second element (index 1) to the end of the list.
        for i in range(1, len(nums)):
            # Compare the current element with the last unique element.
            if nums[last_unique] != nums[i]:
                # If they are different, it means we found a new unique element.
                # Increase 'last_unique' to move to the next position.
                last_unique += 1
                # Update the position of 'last_unique' with the new unique element.
                nums[last_unique] = nums[i]

        # After going through all elements, 'last_unique' will be at the position of the last unique element.
        # We add 1 because 'last_unique' is an index, and we need the count of unique elements.
        return last_unique + 1


# We create an instance of the class 'Solution' to use the method we defined.
solution = Solution()
# Here is the list where we want to remove duplicates.
nums = [1, 1, 2]
# We call the 'removeDuplicates' method and pass 'nums' to it.
# The method will return the new length of the list after duplicates are removed.
new_length = solution.removeDuplicates(nums)
# Print the unique elements up to the new length.
print("The list after removing duplicates:", nums[:new_length])
# Print the new length of the list.
print("New length of the list:", new_length)
