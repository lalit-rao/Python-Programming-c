# def series4(x, n):
#     sum = 0
#     fact = 1
#
#     for i in range(1, n + 1):
#         fact *= i
#         if fact % 2 == 0:
#             sum += x / fact
#
#     return sum
#
#
# x = float(input("Enter the value of x: "))
# n = int(input("Enter the number of terms: "))
# answer = series4(x, n)
# finalAnswer = x + answer
# print(f"The sum of the series is: {finalAnswer}")

def series4(x, n):
    sum = 0
    fact = 1
    i = 1

    while i <= n:
        fact *= i
        if fact % 2 == 0:
            sum += x / fact
            i += 1

    return sum


x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
answer = series4(x, n)
finalAnswer = x + answer
print(f"The sum of the series is: {finalAnswer}")
