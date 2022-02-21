"""
Exercise 31 - Multiple returns
"""
# all four basics in one function, run three times


def Grundrechenarten(a, b):
    if b == 0:
        print("Division is not possible")
        sum = a + b
        dif = a - b
        mul = a * b
        return sum, dif, mul, 0
    else:
        sum = a + b
        dif = a - b
        mul = a * b
        pro = a / b
    return sum, dif, mul, pro


list = [1, 2, 3]
for i in list:
    a = int(input("What is your first number: "))
    b = int(input("What is your second number: "))

    CalcSum, CalcDif, CalcMul, CalcDiv = Grundrechenarten(a, b)
    print("For addition the answer is ", CalcSum)
    print("For subtraction the answer is ", CalcDif)
    print("For multiplication the answer is ", CalcMul)
    print("For division the answer is ", CalcDiv)
    print("")
