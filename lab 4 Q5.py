# def series6(x, n):
#     sum = 0
#
#     for i in range(0, n + 1):
#        sum += 1 / (x ** i)
#
#     return sum
#
#
# x = float(input("Enter the value of x: "))
# n = int(input("Enter the number of terms: "))
# answer = series6(x, n)
# print(f"The sum of the series is: {answer}")

def series6(x, n):
    sum = 0
    i = 0

    while i <=n:
        sum += 1 / (x ** i)
        i += 1
    return sum


x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
answer = series6(x, n)
print(f"The sum of the series is: {answer}")