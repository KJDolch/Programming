"""
Exercise 12 -Slicing of Lists
"""
Nr1 = list(range(20))
Nr2 = list(range(20, 40))
lenght1 = int(len(Nr1))
lenght2 = int(len(Nr2))


print("How do you want to slice:")
slice1 = int(input("lower limit: "))
slice2 = int(input("higher limit: "))

if slice1 < lenght1 and slice2 < lenght1:
    print(Nr1[slice1:slice2])
    print(Nr2[slice1:slice2])

else:
    print("Please give smaller numbers.")
    slice3 = int(input("lower limit: "))
    slice4 = int(input("higher limit: "))

    if slice3 < lenght1 and slice4 < lenght1:
        print(Nr1[slice3:slice4])
        print(Nr2[slice3:slice4])

    else:
        print(Nr1)
        print(Nr2)
