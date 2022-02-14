"""
Exercise 14 - Removing entries
"""


list1 = ["apple", "orange", "banana", "kiwi"]
list2 = ["tomato", "cucumber", "pepper", "salad"]
list3 = ["bread", "pasta", "potato", "rice"]

print(list1)
print(list2)
print(list3)

fruits = input("Which fruit don't you like: ")
vegetables = input("Which vegetable don't you like: ")
carbs = input("Which carbs don't you like: ")

list1.remove(fruits)
list2.remove(vegetables)
list3.remove(carbs)

print(list1)
print(list2)
print(list3)
