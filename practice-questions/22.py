rows = 5

for i in range(rows):
    for j in range(rows):
        if j >= rows - 1 - i and j <= (rows // 2) + i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
