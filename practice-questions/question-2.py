def is_number_palindrome(num):
    if (num<0):
        return False
    original_num = num
    reversed_num = 0

    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num = num // 10

    return original_num == reversed_num

num = int(input("Enter a number: "))
if (is_number_palindrome(num)):
    print("Yes")
else:
    print("No")