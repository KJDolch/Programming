"""
Exercise 22 - Adding and removing
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
# removing two elements, one after the other
Elem1 = set_one.pop()
Elem2 = set_one.pop()
Elem3 = set_two.pop()
Elem4 = set_two.pop()
Elem5 = set_three.pop()
Elem6 = set_three.pop()
Elem7 = set_four.pop()
Elem8 = set_four.pop()
# print the elements
print(Elem1)
print(Elem2)
print(Elem3)
print(Elem4)
print(Elem5)
print(Elem6)
print(Elem7)
print(Elem8)
# add the elements
set_one.add(Elem2)
set_one.add(Elem1)
set_two.add(Elem3)
set_two.add(Elem4)
set_three.add(Elem5)
set_three.add(Elem6)
set_four.add(Elem7)
set_four.add(Elem8)

# print again
print(set_one)
print(set_two)
print(set_three)
print(set_four)
