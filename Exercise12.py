"""
Exercise 12 -Slicing of Lists
"""
# write a program that generates two different lists with contents of your choice
Nr1 = list(range(20))
Nr2 = list(range(20, 40))
lenght1 = int(len(Nr1))
lenght2 = int(len(Nr2))

# let the user input four numbers
print("How do you want to slice:")
slice1 = int(input("lower limit: "))
slice2 = int(input("higher limit: "))
slice3 = int(input("lower limit: "))
slice4 = int(input("higher limit: "))

# if the numbers entered are bigger than the length of the lists, ask a second time for smaller numbers
# slice your lists with the numbers from the user
if slice2 < lenght1 and slice4 < lenght2:
    print("1", Nr1[slice1:slice2])
    print("2", Nr2[slice3:slice4])

else:
    print("Please give smaller numbers.")
    slice5 = int(input("lower limit: "))
    slice6 = int(input("higher limit: "))
    slice7 = int(input("lower limit: "))
    slice8 = int(input("higher limit: "))

    if slice6 < lenght1 and slice8 < lenght1:
        print("3", Nr1[slice5:slice6])
        print("4", Nr2[slice7:slice8])

    # if the new numbers are still too big, generate slices until the last entry of the lists
    else:
        print("5", Nr1[slice5::])
        print("6", Nr2[slice7::])
