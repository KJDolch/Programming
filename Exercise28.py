"""
Exercise 28 - your first functions
"""


def Plus(a, b):
    sum = a + b
    return sum


def Minus(a, b):
    dif = a - b
    return dif


def Mal(a, b):
    mul = a * b
    return mul


def Geteilt(a, b):
    if b == 0:
        print("Not possible")
        return 0
    pro = a / b
    return pro


list = [1, 2, 3]
for i in list:
    a = int(input("What is your first number: "))
    b = int(input("What is your second number: "))

    CalcSum = Plus(a, b)
    print("For addition the answer is ", CalcSum)

    CalcDif = Minus(a, b)
    print("For subtraction the answer is ", CalcDif)

    CalcMul = Mal(a, b)
    print("For multiplication the answer is ", CalcMul)

    CalcDiv = Geteilt(a, b)
    print("For division the answer is ", CalcDiv)
    print("")
