> ## This is the Readme File for The Armstrong Number Program.

- First we take a input from the user that the user wants to find out wheather the number is a Armstrong number or not.
- Any number that is equal to the addition of cube of its digits is a Armstrong Number.
- Ex. 153 = 1^3 + 5^3 + 3^3

Then we declare a varible as Sum = 0, and store the value of number in a temporary variable.

1. The Logic behind this program is that we have to separate out all the digits of the entered nuumber.
2. Then we have to find the cubes of each of them and add the cubes as well.
3. The addition of the cubes will be stored in the sum variable.
4. And at the end we have to check if the value of the sum is equal to the value of the number entered.
5. If it does statisfy the condition, the number is a Armstrong number.
6. Else it isnt a Armstrong number.
    
        while temporaryVariable > 0:
        digit = temporaryVariable % 10
        sum = sum +  digit * digit * digit
        temporaryVariable = temporaryVariable// 10
      
      
- This is the Code that first runs a while loop till the temporaryVariable is greater than 0. 
- Then it separates the digits from the number and then adds the cube of the number to the sum variable.
- Then the temporaryVariable itself is divided by 10 and again the loop goes on.

At last we just have to check if the original number is equal to the sum we got at the end of the loop or not.
