# Factorial of a number using iterative method

# Input number
number = int(input("Enter a Number you want to find the factorial of\n"))
def fact_ittratve(number):
    fact = 1
    for i in range(number):
        fact = fact * (i+1)
    return fact
print("The Factorial of the number:",number, "using iterative methord is:", fact_ittratve(number))
