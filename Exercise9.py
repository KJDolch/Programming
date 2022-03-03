"""
Exercise 9 - Working with range and len
"""
# write a program that generates four lists with different lengths by using the range() function
Nr1 = list(range(20))
Nr2 = list(range(8, 12))
Nr3 = list(range(0, 21, 2))
Nr4 = list(range(1, 21, 2))

print("Lists: ")
print(Nr1)
print(Nr2)
print(Nr3)
print(Nr4)

print("Lenght of lists: ")
c = len(Nr1)
print(c)
c = len(Nr2)
print(c)
c = len(Nr3)
print(c)
c = len(Nr4)
print(c)
# the user should be able to input which lengths he needs
length = int(input("How long should the list be: "))

Nr5 = list(range(length + 1))

# let the program print out the generated lists as well as the corresponding lengths

print(Nr5)
print(length)
