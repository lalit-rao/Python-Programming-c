rows = int(input("Enter the number of rows: "))
k=1
for i in range(rows):
    for j in range(i+1):
        print(k, end=" ")
        k+= 1
    print()