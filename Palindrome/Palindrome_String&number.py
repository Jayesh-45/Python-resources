
#### palindrome of a string

      string = input(("Enter a string: \n"))
      if(string == string[::-1]): 
            print("The string is a palindrome")
      
      else:
           print("Not a palindrome")

#### pallindrome number

     num = int(input("Enter a number: \n"))
     temp = num
     rev = 0
     while(num>0):
       dig = num % 10
       rev = rev * 10 + dig
       num = num//10
     if(temp == rev):
        print("The number is palindrome!")
    else:
       print("Not a palindrome!")
