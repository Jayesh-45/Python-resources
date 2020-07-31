# Here we are importing the "random" module in Python.
# To find a random integer in a perticular range.

import random
# This function generates a random integer from 0 to 50.

var1 = random.randint(0, 50)
print(var1)

# Function to generate a random integer number within a range.

var2 = random.randrange(3,30, 3)
print(var2)

# This is a function that prints a random number within the range 0-1, and the number is multiplied by 100 that makes the decimal point shift two spaces to the right.

var3 = random.random() * 100
print(var3)
