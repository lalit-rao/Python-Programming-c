# Write a program to find the remainder of two integers without using the '%' operator.

def remainder(dividend, divisor):
    if divisor == 0:
        return "Division by zero is not allowed"

    while dividend >= divisor:
        dividend -= divisor

    return dividend


dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))
print("Remainder is: ", remainder(dividend, divisor))