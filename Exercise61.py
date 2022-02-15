"""
Exercise 61 - Checking for values
"""
mylist = ["bread", "milk", "pasta", "pesto", "bananas", "apples", "wine"]

Check1 = input("What is in the fridge: ")
Check2 = input("What is missing in the fridge: ")
Check3 = input("What do you not eat: ")

if Check1 in mylist:
    print("Don't buy it!")
if Check2 not in mylist:
    print("Add it to the shoppinglist")
if Check3 not in mylist:
    print("Don't buy it!")
