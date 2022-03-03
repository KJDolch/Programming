"""
Exercise 20 - Working with tuples
"""
# write a program that dreates four tuple of different lengths
# ask for input: lenght of tuples
one = int(input("How long should be number one: "))
two = int(input("How long should be number two: "))
three = int(input("How long should be number three: "))
four = int(input("How long should be number four: "))
# create tuples with corresponding length
mytuple_one = tuple(range(one))
mytuple_two = tuple(range(two))
mytuple_three = tuple(range(three))
mytuple_four = tuple(range(four))
# ask for input: position of each tuple
five = int(input("Which position do you want to see of number one: "))
six = int(input("Which position do you want to see of number two: "))
seven = int(input("Which position do you want to see of number three: "))
eight = int(input("Which position do you want to see of number four: "))
# print first whole tuple and than the position asked for
print(mytuple_one)
print(mytuple_one[five])
print(mytuple_two)
print(mytuple_two[six])
print(mytuple_three)
print(mytuple_three[seven])
print(mytuple_four)
print(mytuple_four[eight])
# if adding duplicated values (DO NOT use the word 'tuples')
mytuple_five = ("apples", "bananas", "banana", "Apples", "apples")
mytuple = (1, 2, 1)
print(mytuple_five)
print(mytuple)
