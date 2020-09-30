> ### This is the Readme file for the GCD program in python.
- This Program makes using of the user defined functions to find the Greatest Common Divisor of Two Numbers.
- First we input two numbers you want to find the GCD of.
- Then we check if the first number entered is smaller than the second number.
- If it's greater than the second number than we have to swap both the numbers.
- You can use any Methord to swap both the numbers, but here i am using the swapping methord using third variable.

      Number1 = int(input("Enter both the numbers you want to find the GCD of.\n"))
      Number2 = int(input())  
      # We have to swap both the numbers if n1>n2
      if (Number1 > Number2):
        temp = Number1
        Number1 = Number2
        Number2 = temp

- The greatest common divisor (GCD), also called the greatest common factor, of two numbers is the largest number that divides them both.
- For example, the greatest common factor of 20 and 15 is 5, since 5 divides both 20 and 15 and no larger number than 5 divides both of them.

After making sure that the second number is greater than the first, the GCD Function is called.
- The program than jumps in the function.

            gcd = GCD(Number1, Number2)

Here we use a for loop ranging from 1 to the smaller number, to check if the number divides both the entered numbers. 
- The last number than satisfies the condition is the GCD.

            def GCD(a, b):
                  for i in range(1, b):
                        if((a%i==0) and (b%i==0)):
                        gcd = i

                   return gcd

- This is the code for the Function body.
- This function returns the GCD Value and its stored in a variable, then it is displayed on the console.

            gcd = GCD(Number1, Number2) # function called and the returned value is stored in this variable.
            print("The GCD of both the numbers is :",gcd)
        
