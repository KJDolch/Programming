"""
Exercise 23 - Your first loops
"""
# loop for the sum of all numbers von 0 to 21
Sums = 0
for i in range(0, 22):
    Sums = Sums + i
print(Sums)
print("")
# loop for sum of all even numbers
Sums = 0
for i in range(0, 22, 2):
    Sums = Sums + i
(print(Sums))
print("")
# loop for the list in reverse order
list1 = []
for i in range(21, 0, -1):
    list1 += [i]
print("list1", list1)

list2 = []
for i in reversed(range(0, 22)):
    list2.append(i)
print("list2", list2)

list3 = []
for i in reversed(range(0, 22)):
    list3 = list3 + [i]
print("list3", list3)
