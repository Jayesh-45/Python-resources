> ### This is the Readme file for a Python program that displays all the prime numbers in a perticular interval on the console.

#### 1. First it asks the user to enter the value from which the interval starts and also the value at which the interval ends.

#### 2. Then a for loop is initialized that starts the number from the starting value and increments the number till the limit.

    for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end="   ")
