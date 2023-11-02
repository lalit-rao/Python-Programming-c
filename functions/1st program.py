def calculateGmean(a,b):

    mean = (a*b)/(a+b)
    print(mean)

def isGreaterThan(a,b):
    if (a > b):
        print("a is greater than b")
    else:
        print("b is greater than a")

def isLesserThan(a,b):
    if (a < b):
        print("a is lesser than b")
    else:
        print("b is lesser than a")

a = 10
b = 12
isGreaterThan(a,b)
isLesserThan(a,b)
calculateGmean(a,b)

a=12445674
b=231455
isGreaterThan(a,b)
isLesserThan(a,b)
calculateGmean(a,b)
