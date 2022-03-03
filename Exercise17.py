"""
Exercise 17 - Searching in dictionaries
"""
# create a dictionary with at least ten entries
ShoppingList = {}
ShoppingList["Eggs"] = 6
ShoppingList["Flour"] = "500 g"
ShoppingList["Milk"] = "200 ml"
ShoppingList["Butter"] = "200 g"
ShoppingList["salt"] = "some"
ShoppingList["sugar"] = "150 g"
ShoppingList["choclate"] = "100 g"
ShoppingList["hazelnuts"] = "200 g"
ShoppingList["cinnamon"] = "1 Tsp"
ShoppingList["Cherries"] = 10

ShoppingList1 = ShoppingList.copy()

# let the user search the dictionary for a specific entry
search1 = input("What do you search: ")
# if the entry is already present, ask the user for an update of the contents for this entry, if the entry doesn't exist, add it to the dictionary
if search1 in ShoppingList:
    print(ShoppingList[search1])
    content1 = input("Is the content ok: yes or no ")
    if content1 == "yes":
        print(ShoppingList[search1])
    else:
        content1 = input("How much: ")
        ShoppingList[search1] = content1
else:
    amount1 = input("How much: ")
    ShoppingList[search1] = amount1

# run this option at least three times during one call of the program
search2 = input("What do you search: ")
if search2 in ShoppingList:
    print(ShoppingList[search2])
    content2 = input("Is the content ok: yes or no ")
    if content2 == "yes":
        print(ShoppingList[search2])
    else:
        content2 = input("How much: ")
        ShoppingList[search2] = content2
else:
    amount2 = input("How much: ")
    ShoppingList[search2] = amount2

search3 = input("What do you search: ")
if search3 in ShoppingList:
    print(ShoppingList[search3])
    content3 = input("Is the content ok: yes or no ")
    if content3 == "yes":
        print(ShoppingList[search3])
    else:
        content3 = input("How much: ")
        ShoppingList[search3] = content3
else:
    amount3 = input("How much: ")
    ShoppingList[search3] = amount3

# print out the original dictionary and the modified dictionary at the end
print(ShoppingList1)
print(ShoppingList)
