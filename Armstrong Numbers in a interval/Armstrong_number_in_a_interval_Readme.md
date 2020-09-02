# This is the program for Armstrong number in a perticular interval.
- First we input the interval limits for the program.

      lowerLimit = int(input("Enter the lower limit of the interval..\n"))
      upperLimit = int(input("Enter the upper limit of the interval..\n"))


- Any number that is equal to the addition of cube of its digits is a Armstrong Number.
- Ex. 153 = 1^3 + 5^3 + 3^3

- Then we start a for loop ranging from the lower limit to the upper limit that checks all the numbers if they are armstrong number or not.

      for number in range(lowerLimit, upperLimit + 1):
       orderOfTheNumber = len(str(number))
- The number of digits in the number is also important as we have to cube all the digits in the number and add them.
- Then we declare a sum variable and initialize it as sum = 0, and store the value of number in a temmporary variable, as the number will get destroyed during the loop, 
and we have to check if the final value is equal to the original number.

    
        while temporaryVariable > 0:
        digit = temporaryVariable % 10
        sum = sum + digit ** orderOfTheNumber
        temporaryVariable = temporaryVariable// 10
      
      
- This is the Code that first runs a while loop till the temporaryVariable is greater than 0. 
- Then it separates the digits from the number and then adds the cube of the number to the sum variable.
- Then the temporaryVariable itself is divided by 10 and again the loop goes on.

At last we just have to check if the original number is equal to the sum we got at the end of the loop or not.
