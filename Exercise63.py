"""
Exercise 63 - More for loops
"""
# create a list with 20 numbers which are not sorted
# list = [1, 22, 3, 24, 5, 26, 7, 28, 9, 210, 11, 212, 13, 214, 15, 216, 17, 18, 219, 20]
import random

random_list = []
for i in range(0, 20):
    random_list.append(random.randint(1, 50))
print(random_list)


# loop for all elements and with sum at the end
sum = 0
for i in random_list:
    sum = sum + i
    # sum += elem
print("")
print(sum)

# asking for number
number = int(input("What is your favorit number: "))

print(
    "So let's see if the numbers are bigger or smaller than your favorit number "
    + str(number)
)
# loop for question if number is bigger or smaller
for i in random_list:
    if i > number:
        print(str(i) + " is bigger")
    elif i < number:
        print(str(i) + " is smaller")
    else:
        print("Your number is in the list!")
