 # Factorial of a number using recursive functions
 
# Input Number
number = int(input("Enter a Number you want to find the factorial of\n"))
def fact_recursion(n):
    if n == 1:
        return 1
    else:
        return n * fact_recursion(n-1)

print("The Factorial of the number:",number, "using recursion is", fact_recursion(number))
