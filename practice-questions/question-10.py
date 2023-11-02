# Write a program to find the area and circumference of a circle.

def area(r):
    return r ** 2


def circumference(r):
    return 2 * 3.14 * r


radius = int(input("Enter the radius of the circle: "))
print("Area of the circle is: ", area(radius))
print("Circumference of the circle is: ", circumference(radius))
