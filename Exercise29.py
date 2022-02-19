"""
Exercise 29 - Functions with simple loops
"""

# the first function should take a list as argument and return the sum of all elemts in the list, calculated by a loop


def function1(inputlist):
    sum = 0
    for i in range(len(inputlist)):
        sum += i
    return sum


list1 = range(22)
SUM = function1(list1)
print(SUM)

list3 = range(0, 21, 2)
SUM = function1(list3)
print(SUM)

# the second function should also take a list and return a list which the contents of the handed over list are reversed


def function2(a):
    Reverse = []
    for i in reversed(range(len(a))):
        Reverse += [i]
    return Reverse


list2 = range(22)
REV = function2(list2)
print(REV)
