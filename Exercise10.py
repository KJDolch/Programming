"""
Exercise 10 - Skipping parts with range
"""
# write a program that generates different lists with the help of the range functions
# the program should generate a list that doesn't start at 0
# the program should generate two other lists that skip some numbers (three arguments for range)
# Don't forget to print out all three lists at the end
Nr1 = list(range(8, 20))
Nr2 = list(range(8, 21, 2))
Nr3 = list(range(9, 21, 2))

print("List starting at 8: ")
print(Nr1)
print("Even numbers: ")
print(Nr2)
print("Uneven numbers: ")
print(Nr3)
