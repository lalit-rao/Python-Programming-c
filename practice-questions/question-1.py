# string is palindrome or not use string slicing

def is_palindrome(s):
    s = s.replace("", "").lower()
    reversed_s = s[::-1]

    return s == reversed_s


string = str(input("Enter a string: "))
if (is_palindrome(string)):
    print("Yes")
else:
    print("No")