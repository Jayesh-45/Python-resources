# This program converts A Decimal number to it's equivalent binary, octal and hexadecimal numbers.
""" Decimal Number:- Base 10 
    Binary Number:- Base 2
    Octal Number:- Base 8
    Hexadecimal Number:- Base 16
    """

# First we input a decimal number.

dec = int(input("Enter a Decimal Number"))

print(bin(dec)," is the Binary Equivalent of ",dec)
print(oct(dec)," is the Octal Equivalent of ",dec)
print(hex(dec)," is the Hexadecimal Equivalent of ",dec)

