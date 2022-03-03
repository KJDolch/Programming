"""
Exercise 13 - Slicing with a :
"""
# write a program that generates a list with the help of the range function
List = list(range(20))
# the user should input the length of the wanted list and than input four other different numbers that can be used for slicing the list
lenght = int(input("How long should the list be: "))

print(List[:lenght])
NewList = List[:lenght]

# the first number should be an endpoint od the new list, the second number a starting point and the other two numbers ashould represent skips you can do with Slicing
# print out the new lists
endpoint1 = int(input("Where should your list ends: ")) + 1

print(NewList[:endpoint1])

start = int(input("Startpoint: "))

print(NewList[start::])

skip1 = int(input("How do you want to skip: "))

print(list(range(start, endpoint1, skip1)))

skip2 = int(input("Another way to skip: "))

print(list(range(start, endpoint1, skip2)))
