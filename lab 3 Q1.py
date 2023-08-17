numbers = []
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    else:
        maximum = max_num
print("The maximum number is:", max_num)

# numbers = []
# for i in range(10):
#     num = int(input(f"Enter number {i + 1}: "))
#     numbers.append(num)
# numbers.sort()
# maximum = numbers[0]
# print("The maximum number is: ", maximum)