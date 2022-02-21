"""
Exercise 64 - Keywords in Python
"""
# Create a list with at least 15 random entries
# Iterate over it with a for loop and add up the elements
# Create one if statement in your loop that can’t be true a
# add a pass
# Include a second if statement in your loop that breaks the loop if your sum gets bigger than a threshold (you chose)
# Include a third if statement in your loop that uses continue if the current entry of your list is in a specific range, eg. 50 to 60, and prints out something in all other cases (use else)
# Print out the sum and the number of index

import random

randomlist1 = [random.randrange(1, 100) for i in range(15)]
print(randomlist1)

sum = 0
for i in range(len(randomlist1)):
    sum += randomlist1[i]
    if sum < 0:
        pass
    elif sum > 200:
        break
    elif 50 <= sum <= 199:
        continue
    else:
        print("There you go")
        print(sum)
        print(i)
print(sum)
print(i)
