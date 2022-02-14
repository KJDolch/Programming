"""
Exercise 11 - Longer list
"""

Nr1 = list(range(20))
Nr2 = list(range(20, 40))
Nr3 = list(range(40, 60))
Nr4 = list(range(40, 60))
Nr5 = list(range(-20, 0))
Nr6 = list(range(-40, -20))

print("Lists:")
print(Nr1)
print(Nr2)
print(Nr3)
print(Nr4)
print(Nr5)
print(Nr6)

print("Appending:")
Nr1.append(Nr3)
print(Nr1)
Nr2.append(Nr4)
print(Nr2)

print("Extending:")
Nr1.extend(Nr5)
print(Nr1)
Nr2.extend(Nr6)
print(Nr2)
