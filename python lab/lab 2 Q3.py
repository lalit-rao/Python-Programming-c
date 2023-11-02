def a(d):
    c = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    return c[d]


def b(number):
    word_number = str(number)
    for digit in word_number:
        print(a(int(digit)), end=" ")


number = int(input("Enter the numbers to convert into words: "))
print("Answer", end=" ")
b(number)
