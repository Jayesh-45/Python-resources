# This is a program that prints both the star patterns.

# Entering 0 prints the rows in increasing order of *'s.
# Entering 1 prints the rows inn decreasing order of *'s.
# First you enter the number of rows you want to print.
# Then you select the pattern

num = int(input("Enter the num of rows you want to print..\n"))
x = int(input("Enter pattern 0/1..\n"))

if x == 0:
    count = 0
    while(count<=num):
        print("* " * count )
        count =count + 1
elif x ==1:
    count = num
    while(count>0):
        print("* " * count)
        count = count - 1
