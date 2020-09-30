# Program to check Armstrong numbers in a interval

lowerLimit = int(input("Enter the lower limit of the interval..\n"))
upperLimit = int(input("Enter the upper limit of the interval..\n"))

for number in range(lowerLimit, upperLimit + 1):
    orderOfTheNumber = len(str(number))

    sum = 0
    temporaryVariable = number
    
    while temporaryVariable > 0:
        digit = temporaryVariable % 10
        sum = sum + digit ** orderOfTheNumber
        temporaryVariable = temporaryVariable // 10

    if number == sum:
        print(number)
