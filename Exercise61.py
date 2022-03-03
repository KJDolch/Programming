"""
Exercise 61 - Checking for values
"""
# write a program that generates a list with contents of your choice
mylist = ["bread", "milk", "pasta", "pesto", "bananas", "apples", "wine"]
# Now let the user input at least three different things
Check1 = input("What is in the fridge: ")
Check2 = input("What is missing in the fridge: ")
Check3 = input("What do you not eat: ")
# check wheather these inputs are part of your list or not
# print out an appropriate answer
if Check1 in mylist:
    print("Don't buy it!")
if Check2 not in mylist:
    print("Add it to the shoppinglist")
if Check3 not in mylist:
    print("Don't buy it!")
