# [0 1 1 2 3 5 8 13 21] This is the fibonacci series.
# The next number is found by adding up the two numbers before it:

# Here we chose the index number of the Fibonnaci Series Number you want to find out.

print("Enter the index number of the fibonnaci series number you want to find out: \n")
number = int(input())
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

print("The Number at the index position of:", number, "is:",fibo(number))
