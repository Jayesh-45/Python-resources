### This is a program about finding out the factorial of a given number.

> #### Here we have two choices to find out the factorial.

1. By Iterative method.
2. By Recursive method.

In the Iterative method, we use the for loop which iterates in the range of 0 to the entered number.
- Every time the statement is executed, the value of i is incremented by 1, until the value becomes equal to the original number.

for i in range(number):

    fact = fact * (i+1)
    return fact

- This is the logic behind the solution, where first fact variable is initialised from 1, and the value the value of fact is calculated as fact * i, till the loop runs.

- Finally the value of fact is returned and the value is printed on the screen.
