"""
Exercise 13 - Slicing with a :
"""

List = list(range(20))

lenght = int(input("How long should the list be: "))

print(List[:lenght])
NewList = List[:lenght]

endpoint1 = int(input("Where should your list ends: ")) + 1

print(NewList[:endpoint1])

start = int(input("Startpoint: "))

print(NewList[start::])

skip1 = int(input("How do you want to skip: "))

print(list(range(start, endpoint1, skip1)))

skip2 = int(input("Another way to skip: "))

print(list(range(start, endpoint1, skip2)))
