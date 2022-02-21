"""
Exercise 32 - Multiple returns from lists
"""
# one function for the return of the sum and the reversed list with just one for-loop
def MultiReturns(inputlist):
    sum = 0
    Reverse = []
    for i in reversed(range(len(inputlist))):
        sum += i
        Reverse += [i]
    return sum, Reverse


list1 = range(22)
Sum, Rev = MultiReturns(list1)
print("The sum of the list is: ", Sum)
print("The reverse list is: ", Rev)
