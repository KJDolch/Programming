"""
Exercise 17 - Searching in dictionaries
"""
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

search1 = input("What do you search: ")

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

print(ShoppingList1)
print(ShoppingList)
