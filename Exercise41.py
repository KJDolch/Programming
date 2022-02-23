"""
Exercise 41 - Exceptions on inputs
"""
# write a program that runs a simple division
# generate a random integer and divide it through an integer inputted by user
import random

randomnumber = random.randint(1, 100)

i = 0
while i < 3:
    try:
        number = int(input("What is your favorit number: "))
        # div = None
        div = randomnumber / number
    # create an exception for wrong inputs (a string for example)
    except ValueError:
        print("Please type in a number")
    # create a second exception to handle division by zero
    except ZeroDivisionError:
        print("Division by zero is not possible")
    # both exceptions should belong to same try:
    except:
        print("Unknown Error")
    else:
        print(number)
        print(div)
    i += 1
# print out the result of the divison at the end and try several different inputs
