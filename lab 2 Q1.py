a = float(input("Please enter your purchase value? "))
if a > 8000:
    b = ((a - (a * 0.50)) * 0.50)
    print("The final value of your purchase after discount is ", b)

elif 5000 <= a <= 8000:
    b = a * 0.50 -((a - (a * 0.50)) * 0.20)
    print("The final value of your purchase after discount is ", b)

elif a < 5000:
    print("The final value of your purchase with no discount is ", a)

else:
    print("Invalid value")
