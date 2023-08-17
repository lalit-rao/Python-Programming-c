# numbers = []
# for i in range(10):
#     num = int(input(f"Enter the number {i + 1}: "))
#     numbers.append(num)
# numbers.sort()
# second_maximum = numbers[1]
# print("The second maximum number is: ", second_maximum)


numbers = []
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
max1 = max2 = 0

for num in numbers:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num
        second_max = num

print("The second maximum number is:", second_max)