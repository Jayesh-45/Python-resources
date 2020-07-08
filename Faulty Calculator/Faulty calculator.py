# A calculator that solves all the problems correctly but not these problems.
# 45 * 3 = 155, 56 + 9 = 77, 56 / 6 = 4.
opp = input("Enter the operator from + * / - % \n")
num1 = int(input("Enter the Operand 1\n"))
num2 = int(input("Enter the Operand 2\n"))
if opp == "*":
    if num1 == 45 and num2 == 3:
        print("Value is 155")
    else:
        print("value is ",num1 * num2)
elif opp == "+":
    if num1 == 56 and num2 == 9:
        print("Value is 77")
    else:
        print("value is ",num1 + num2)
elif opp == "/":
    if num1 == 56 and num2 == 6:
        print("Value is 4")
    else:
        print("value is ",num1/num2)
elif opp == "-":
    print("Value is", num1-num2)
elif opp == "%":
    print("Value is", num1%num2)
