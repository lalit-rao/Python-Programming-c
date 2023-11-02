# WAP to calculate the final price of a product after following criteria of discount.
# Cost price				discount
# >8000					50%+50%
# 5000-8000				50%+20%
# <5000					0%

def calculate_final_price(cost_price):
    if cost_price > 8000:
        discount = ((cost_price * 0.50) * 0.50)
        cost_price = cost_price - discount
        print("The final price is: ", cost_price)

    elif cost_price >= 5000 and cost_price <= 8000:
        discount = ((cost_price * 0.50) * 0.20)
        cost_price = cost_price - discount
        print("The final price is: ", cost_price)

    else:
        print("The final price is: ", cost_price)


cost_price = int(input("Enter the cost price: "))
calculate_final_price(cost_price)
