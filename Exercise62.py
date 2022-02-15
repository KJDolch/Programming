"""
Exercise 62 - Inserting values
"""
listA = list(range(20))
listB = list(range(40))
listC = list(range(40, 60))

print("listA:")
print(listA)
print("listB:")
print(listB)
print("listC:")
print(listC)

choice = input("Which list do you want to change: A, B or C: ")
index = int(input("Where do you want to insert: "))
value = input("Which number do you want to insert: ")

if choice == "A":
    print("New listA: ")
    if index in listA:
        listA.insert(index, value)
        print(listA)
    else:
        print("Failed")

elif choice == "B":
    print("New listB: ")
    if index in listB:
        listB.insert(index, value)
        print(listB)
    else:
        print("Failed")

elif choice == "C":
    print("New listC: ")
    if index in listC:
        listC.insert(index, value)
        print(listC)
    else:
        print("Failed")
