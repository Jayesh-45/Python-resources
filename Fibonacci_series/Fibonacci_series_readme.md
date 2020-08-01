> ## This is the Readme File for the Fibonacci series.

### [0 1 1 2 3 5 8 13 21] This is the fibonacci series.

The simple logic of this series is that the series starts from the two numbers 0 and 1 and the next number is formed by adding the previous two numbers.

- 0+1 becomes 1, and 1+1 becomes 2, and 1+2 becomes 3, and so on.

Here we input the index number of the number we want to find out from the fibonacci series we want to find out.


  def fibo(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


The simple logic is the number is addition of fibo number at (n-1)th postion and (n-2)th position.

This addition becomes the number at that position and the program continues till the nth postion is 0 where the value is 0 and when the nth position is 1 where the value is 1 itself. 
