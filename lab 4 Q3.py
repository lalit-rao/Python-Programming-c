# def series3(n):
#     sum = 0
#
#     for i in range(1, n + 1):
#         sum += i * (i + 1) / (i + 2)
#
#     return sum
#
#
# n = int(input("Enter the number of terms: "))
# answer = series3(n)
# print(f"The sum of the series for {n} terms is: {answer}")

def series3(n):
    sum = 0
    i = 1

    while i <= n:
        sum += i * (i + 1) / (i + 2)
        i += 1

    return sum


n = int(input("Enter the number of terms: "))
answer = series3(n)
print(f"The sum of the series for {n} terms is: {answer}")
