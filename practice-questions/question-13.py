#  Compute the grade of a student based on the following criteria for marks:
#
# Marks    Grade
# >=80        A
# >=70        B
# >=60        C
# >=50        D
# >=40        E
# <40         F

marks = int(input("Enter your marks: "))
if marks >= 80:
    print("Your grade is A")
elif marks >= 70:
    print("Your grade is B")
elif marks >= 60:
    print("Your grade is C")
elif marks >= 50:
    print("Your grade is D")
elif marks >= 40:
    print("Your grade is E")
else:
    print("Your grade is F")
