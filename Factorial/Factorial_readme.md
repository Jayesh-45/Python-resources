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

----
In the Recursive Method, Recursion of function is used in which functions call themselves until the condition is satisfied.

- A function that calls itself during its execution is a reursive function.
- This enables the function to call itself several times and at the end if each iteration a result is ouputted.


def fact_recursion(n):


    if n == 1:
        return 1
    else:
        return n * fact_recursion(n-1)

- This is the code that shows how recursion can be used to calculate the factorial of a number.
- The program calls itself until the number is one and the value of the factorial is returned.
