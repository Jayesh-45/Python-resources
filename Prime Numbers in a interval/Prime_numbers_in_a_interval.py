# Python program to display all the prime numbers within an interval


lower = int(input("Enter the Number from which the interval starts..\n"))
upper = int(input("Enter the Number at which the interval ends..\n"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end="   ")
