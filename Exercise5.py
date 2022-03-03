"""
Exercise 5 - Big numbers
"""
# Write a program that asks for two numbers
Number1 = input("Give me a number: ")
Number2 = input("Give me a second Number: ")

# oder Number1 = int(input("Give me a number: "))
# Number2 = int(input("Give me a second one: "))
# sum = Number1 + Number2

sum = int(Number1) + int(Number2)
print(sum)
# print(type(sum))
# If the sum of the numbes is greater than 100, print "That is a big number"
if sum > 100:
    print("That is a big number")
# if the sum is between ten and 100, print "That is a mediocre number"
elif 10 < sum < 100:
    # oder elif sum > 10 and sum < 100:
    print("That is a medicore number")
# if the sum is between 5 and ten, print "That is a small number"
elif 5 < sum < 10:
    print("That is a small number")

elif sum == 10:
    print("Jackpot")

elif sum == 100:
    print("oooohhh")
# in all other cases print "That is a very small number"
else:
    print("This is a very small number")
