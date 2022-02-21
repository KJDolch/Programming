"""
Exercise 33 - New modules
"""
# write a program that asks the user to guess a specific number
number = int(input("Guess a number: "))

# generate a random number between 0 and 99, search the library (https://docs.python.org/3/library/) to find a module and a function for this task
import random

randomnumber = random.randrange(99)
print(randomnumber)
# generate a while loop that asks for a guess as long as the user didn't guess right
# print out hints if the user is lower or higher than the random number

i = 0
while i < len(range(99)):
    if number == randomnumber:
        print("Your guess was right! The number was ", randomnumber)
        break
    elif number < randomnumber:
        print("Your guessed number was too small")
    elif number > randomnumber:
        print("Your guessed number was too big")
    number = int(input("Guess again: "))
    i += 1
# Count the number of guesses the user needed and print them out after the user guessed correctly
print("You nedded", i + 1, "guesses")

# anderer Lösungsweg:
randomnumber = random.randint(0, 100)
found = False
count = 0
while found == False:
    Guess = int(input("Take a guess: "))
    count += 1
    if Guess > randomnumber:
        print("Your guess was too big")
    elif Guess < randomnumber:
        print("Your guess was too small")
    elif Guess == randomnumber:
        print("You are right")
        print("You needed", count, "guesses.")
        found = True
    if count == 50:
        print("You were too slow")
        break
