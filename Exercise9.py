"""
Exercise 9 - Working with range and len
"""

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

lenght = int(input("How long should the list be: "))

if lenght <= 4:
    print(Nr2)
elif 4 < lenght <= 10:
    print(Nr4)
elif 10 <= lenght <= 20:
    print(Nr3)
else:
    print(Nr1)
