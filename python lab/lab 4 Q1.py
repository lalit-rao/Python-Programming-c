def series1(n):
    Sum = 0
    fact = 1

    for i in range(1, n + 1):
        fact *= i
        Sum += i / fact

    return Sum


n = int(input("Enter the number of terms: "))
answer = series1(n)
print(f"The sum of the series for {n} terms is: {answer}")

def series1(n):
    Sum = 0
    fact = 1
    i = 1

    while i <= n:
        fact *= i
        Sum += i / fact
        i += 1

    return Sum


n = int(input("Enter the number of terms: "))
answer = series1(n)
print(f"The sum of the series for {n} terms is: {answer}")
