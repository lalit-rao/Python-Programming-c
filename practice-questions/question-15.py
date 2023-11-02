# WAP to check whether an integer is palindrome or not.

def check_palindrome(number):
    original_number = number
    reverse_number = 0
    while number > 0:
        remainder = number % 10
        reverse_number = (reverse_number * 10) + remainder
        number = number // 10

    if original_number == reverse_number:
        print("The number is palindrome.")
    else:
        print("The number is not palindrome.")


number = int(input("Enter the number: "))
check_palindrome(number)
