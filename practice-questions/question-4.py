def series2(n):
    if n < 0:
        return False
    else:
        result = n - 1 if n % 2 == 0 else n + 1
        print(result)


n = int(input("Enter a number: "))
print(series2(n))
