def series4(x, n):
    sum = 0
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
        if factorial % 2 == 0:
            sum += x / factorial

    return sum


x = float(input("Enter the value of x: "))
n = int(input("Enter the number of terms: "))
answer = series4(x, n)
finalAnswer = x + answer
print(f"The sum of the series is: {finalAnswer}")
