def series6(n):
    term = 1
    sum = 0

    for i in range(n):
        sum += term
        term = term * 10 + 1

    return sum


n = int(input("Enter the number of terms in the series: "))
answer = series6(n)
print(f"The sum of the series for {n} terms is: {answer}")
