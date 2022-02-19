"""
Exercise 24 - 3 more loops
"""
# creating a random list with numbers between 0 and 99 with unknown length
import random

rand = random.randint(0, 100)
list1 = list(range(rand))
print(list1)
random.shuffle(list1)
print(list1)
# Searching for a specific number in an integer list of unknown length
number = int(input("Which number do you search for: "))
i = 0
while i < len(list1):
    if list1[i] == number:
        print("Found it!")
        break  # stops the loop if number is found
    i += 1
else:
    print("Wrong choice! Your number " + str(number) + " is not in the list!")


# Multiplying all elements with each other of an integer list of unknwon length
i = 0
mult = 1
while i < len(list1):
    if i != 0:
        mult = mult * i
        # or mult *= list1[i]
    i += 1
print(mult)

# printing out the contents of a string list of unknown length elementwise
list2 = ["Apples", "Bananas", "Kiwis"]
i = 0
while i < len(list2):
    print(list2[i])
    i += 1
