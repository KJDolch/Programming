"""
Exercise 36 - Working with constants
"""
import math


nr1 = int(input("Give me one number: "))
nr2 = int(input("Give me a second number: "))
if nr1 == 0:
    print("Wrong choice, the number must be bigger than 0")
    nr1 = int(input("Give me one number: "))
    nr2 = int(input("Give me a second number: "))
elif nr2 == 0:
    print("Wrong choice, the number must be bigger than 0")
    nr1 = int(input("Give me one number: "))
    nr2 = int(input("Give me a second number: "))


ask = int(
    input(
        "With which number do you want to multiply your numbers?\n 1) Pi, 2) Euler number or 3) Tau? "
    )
)


if ask == 1:
    nr3 = nr1 * math.pi
    nr4 = nr2 * math.pi
    print(math.exp(nr3))
    print(math.log(nr3, nr4))
    print(math.log(nr3, 2))
    print(math.log(nr3, 10))
    print(math.pow(nr3, nr4))
    print(math.sqrt(nr3))
    print(math.cos(nr3))
    print(math.sin(nr3))
    print(math.tan(nr3))
    if -1 < nr3 < 1:
        print(math.acos(nr3))
        print(math.asin(nr3))
        print(math.atan(nr3))
elif ask == 2:
    nr3 = nr1 * math.e
    nr4 = nr2 * math.e
    print(math.exp(nr3))
    print(math.log(nr3, nr4))
    print(math.log(nr3, 2))
    print(math.log(nr3, 10))
    print(math.pow(nr3, nr4))
    print(math.sqrt(nr3))
    print(math.cos(nr3))
    print(math.sin(nr3))
    print(math.tan(nr3))
    if -1 < nr3 < 1:
        print(math.acos(nr3))
        print(math.asin(nr3))
        print(math.atan(nr3))
elif ask == 3:
    nr3 = nr1 * math.tau
    nr4 = nr2 * math.tau
    print(math.exp(nr3))
    print(math.log(nr3, nr4))
    print(math.log(nr3, 2))
    print(math.log(nr3, 10))
    print(math.pow(nr3, nr4))
    print(math.sqrt(nr3))
    print(math.cos(nr3))
    print(math.sin(nr3))
    print(math.tan(nr3))
    if -1 < nr3 < 1:
        print(math.acos(nr3))
        print(math.asin(nr3))
        print(math.atan(nr3))
