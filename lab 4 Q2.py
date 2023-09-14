def series2(n):
    sum = 0
    fact = 1

    for i in range(1, n + 1):
        fact *= i
        sum += (i ** 2) / fact

    return sum


n = int(input("Enter the number of terms: "))
answer = series2(n)
print(f"The sum of the series for {n} terms is: {answer}")
