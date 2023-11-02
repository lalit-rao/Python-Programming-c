number = int(input("Enter a number: "))
temporary = number
rev = 0
while number > 0:
    a = number % 10
    rev = rev * 10 + a
    number = number // 10
if temporary == rev:
    print("This number is a Palindrome!")
else:
    print("This number is not a Palindrome!")
