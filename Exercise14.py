"""
Exercise 14 - Removing entries
"""
# write a program that generates at least three different lists

list1 = ["apple", "orange", "banana", "kiwi"]
list2 = ["tomato", "cucumber", "pepper", "salad"]
list3 = ["bread", "pasta", "potato", "rice"]
# print these lists out
print(list1)
print(list2)
print(list3)
# ask the user for one entry from each list he wants to have removed
fruits = input("Which fruit don't you like: ")
vegetables = input("Which vegetable don't you like: ")
carbs = input("Which carbs don't you like: ")
# let the program remove the entry
list1.remove(fruits)
list2.remove(vegetables)
list3.remove(carbs)
# print out the new lists
print(list1)
print(list2)
print(list3)
