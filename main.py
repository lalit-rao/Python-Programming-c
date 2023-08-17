numbers = []
for i in range(3):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

numbers.sort()

second_maximum = numbers[1]
print("The second maximum number is:", second_maximum)
