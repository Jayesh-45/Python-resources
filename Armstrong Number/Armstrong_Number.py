# This is the program for Armstrong number.

print("This is the program for Armstrong number..")
num = int(input("Enter the number you want to check:\n"))

sum = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum = sum +  digit * digit * digit
    temp = temp// 10

if num == sum:
    print(num,"is a Armstrong Number..")

else:
    print(num,"is not a Armstrong Number..")

