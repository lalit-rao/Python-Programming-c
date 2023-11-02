rows = 5

for i in range(rows):
    for j in range(rows):
        if j>=rows-i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()