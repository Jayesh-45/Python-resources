def GCD(a, b):
    for i in range(1, b):
        if((a%i==0) and (b%i==0)):
            gcd = i
    return gcd

Number1 = int(input("Enter both the numbers you want to find the GCD of.\n"))
Number2 = int(input())    # We have to swap both the numbers if n1>n2
if (Number1 > Number2):
    temp = Number1
    Number1 = Number2
    Number2 = temp

gcd = GCD(Number1, Number2)
print("The GCD of both the numbers is :",gcd)
