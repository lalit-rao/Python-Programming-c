number = int(input("Enter a number: "))
print("Your number is: ", number)

if (number < 0):
    print("The number is negative!")
elif (number > 0):
    if (number <= 10 and number >= 1):
        print("The number is between 0 and 10!")
    elif(number <= 20 and number >= 11):
        print("The number is between 11 and 20!")
    else:
        print("The number is greater than 20!")
else:
    print("The number is zero!")