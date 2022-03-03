"""
Exercise 35 - Working with math
"""
# wirte a program that takes two numbers (x and y) from the user and calculates new values with the help of the math functions on the previous slides (exp, log, log2, log10, pow, sqrt, cos, sin, tan, acos, asin, atan)
import math

nr1 = int(input("Give me one number: "))
nr2 = int(input("Give me a second number: "))
print("")
# print out the results
print(math.exp(nr1))
print(math.log(nr1, nr2))
print(math.log(nr1, 2))
print(math.log(nr1, 10))
print(math.pow(nr1, nr2))
print(math.sqrt(nr1))
print(math.cos(nr1))
print(math.sin(nr1))
print(math.tan(nr1))
if -1 < nr1 < 1:
    print(math.acos(nr2))
    print(math.asin(nr2))
    print(math.atan(nr2))
