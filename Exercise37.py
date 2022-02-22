"""
Exercise 37 - Random generator
"""
# write a program that generates several random numbers
import random

# let the user input the ranges for three random integers
input("You have to pick the ranges three times:\n")
ask1 = int(input("First range: Pick a number for the lower range: "))
ask2 = int(input("an for the higher range: ")) + 1
ask3 = int(input("Second range: Pick a number for the lower range: "))
ask4 = int(input("an for the higher range: ")) + 1
ask5 = int(input("Third range: Pick a number for the lower range: "))
ask6 = int(input("an for the higher range: ")) + 1

nr1 = random.randint(ask1, ask2)
print(nr1)
nr2 = random.randint(ask3, ask4)
print(nr2)
nr3 = random.randint(ask5, ask6)
print(nr2)

# let the user choose how many random floats between 0 and 1 should be created
ask7 = int(input("How many random floats should be created? "))
list1 = []
for i in range(ask7):
    x = random.random()
    list1.append(x)
    print(x)
print(list1)

# let the user put in at least two mu and two sigma to create normal distribution values
ask8 = int(input("How often do you want to create a normal distribution? "))
list2 = []
for i in range(ask8):
    ask9 = int(input("Give a value for mu: "))
    ask10 = int(input("Give a value for sigma: "))
    y = random.gauss(ask9, ask10)
    z = random.gauss(ask10, ask9)
    list2.append(y)
    list2.append(z)
    print("The first way:", random.gauss(ask9, ask10))
    print("The reversed way:", random.gauss(ask10, ask9))
print("list2:", list2)
# put all generated values in alist, print the list, shuffle the list and print it again

list3 = [
    nr1,
    nr2,
    nr3,
]
list3.extend(list1)
list3.extend(list2)
print(list3)
random.shuffle(list3)
print(list3)
