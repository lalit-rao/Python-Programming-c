def series7(x, n):
    sum = 1
    a = -1
    exponent = 2
    factorial = 1

    for i in range(1, n):
        iniAnswer = a * (x ** exponent) / (factorial ** exponent)
        sum += iniAnswer
        a *= -1
        exponent += 2

    return sum


x = float(input("Enter the value of x (in radians): "))
n = int(input("Enter the number of terms: "))

answer = series7(x, n)
print(f"Answer is: {answer}")
