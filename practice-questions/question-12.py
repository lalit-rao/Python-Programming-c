# Write a program to determine if a given year is a leap year.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter the year: "))
if is_leap_year(year):
    print("It is a leap year")
else:
    print("It is not a leap year")
