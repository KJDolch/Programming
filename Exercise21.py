"""
Exercie 21 - working with sets
"""

# ask for input: lenght of sets
one = int(input("How long should be number one: "))
two = int(input("How long should be number two: "))
three = int(input("How long should be number three: "))
four = int(input("How long should be number four: "))
# creates the four sets
set_one = set(range(one))
set_two = set(range(two))
set_three = set(range(three))
set_four = set(range(four))
# prints the for sets
print(set_one)
print(set_two)
print(set_three)
print(set_four)
# try to have duplicated values in one set
set_five = {1, 2, 2, 3, 1}
print(set_five)
print(type(set_five))
# try to add a number:
set_five.add(10)
print(set_five)
# try to add a string to set
set_five.add("ten")
print(set_five)
