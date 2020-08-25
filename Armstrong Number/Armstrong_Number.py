# This is the program for Armstrong number.

print("This is the program for Armstrong number..")
number = int(input("Enter the number you want to check:\n"))

sum = 0
temporaryVariable = number

while temporaryVariable > 0:
    digit = temp % 10
    sum = sum +  digit * digit * digit
    temporaryVariable = temporaryVariable// 10

if number == sum:
    print(number,"is a Armstrong Number..")

else:
    print(number,"is not a Armstrong Number..")
