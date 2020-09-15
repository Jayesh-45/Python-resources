### > This is the Readme file for the GCD program in python.
- This Program makes using of the user defined functions to find the Greatest Common Divisor of Two Numbers.
- First we input two numbers you want to find the GCD of.
- Then we check if the first number entered is greater than the second number.
- If it's smaller than the second number than we have to swap both the numbers.
- You can use any Methord to swap both the numbers, but here i am using the swapping methord using third variable.

      Number1 = int(input("Enter both the numbers you want to find the GCD of.\n"))
      Number2 = int(input())  
      # We have to swap both the numbers if n1>n2
      if (Number1 > Number2):
        temp = Number1
        Number1 = Number2
        Number2 = temp
