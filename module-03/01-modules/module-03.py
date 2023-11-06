# Import the math module to access mathematical functions and constants
import math
# Import the random module to generate random numbers
import random

# Print the square root of 10 using the math module's sqrt function
print(math.sqrt(10))
# Print the value of PI from the math module
print(math.pi)

# Generate a random integer between 10 and 20 using the random module's randint function
random_value = random.randint(10, 20)
# Print the randomly generated number and its square root using the math module's sqrt function
print(
    f"The random number is {random_value} and its square root is {math.sqrt(random_value)}"
)
