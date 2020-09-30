> ## This is the Readme file for the Star pattern program in Python.

0 prints the rows in increasing order of *'s.

1 prints the rows inn decreasing order of *'s.

First we take the input for num of rows you want and then we take the input for the type of pattern we want to display.

    if x == 0:
      count = 0
      while(count<=num):
        print("* " * count )
        count =count + 1
    elif x == 1:
      count = num
      while(count>0):
        print("* " * count)
        count = count - 1
        
This is the code using if and else statement for printing the star pattern.
