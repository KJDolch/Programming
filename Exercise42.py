"""
Exercise 42 - Being an Esper
"""
# we want to write a more complex program in which the user guesses a number form 1, 2 or 3. The program should run 25 tries for the user and count how often he guessed right (while loop). The program should raise an exception if the user put in a number outside the range of 1 to 3 and another exception for inputs that weren't integer. Count how many tries the user needed to finish the 25 iterations (in the finally command).
import random

loops = 0
score = 0
i = 0
while i < 5:
    randomnumber = random.randint(1, 3)
    try:
        number = int(input("Guess a number: "))
        if number not in [1, 2, 3]:
            raise RuntimeError("Your number is out of range!")
    except RuntimeError:
        print("Your number is not within the range!")
    except ValueError:
        print("Please type a number!")
    else:
        if number == randomnumber:
            score += 1
            print("You win!", score)
        i += 1
    finally:
        loops += 1
print("You had ", score, "times the right number")
print("You nedded: ", loops, "guesses for 5 right attempts!")
