"""
Exercise 6 - Comparing Numbers
"""
# write a program that gets four numbers as input from the user
Nr1 = int(input("Give me one number: "))
Nr2 = int(input("Give me another one: "))
Nr3 = int(input("and one more: "))
Nr4 = int(input("and a last one: "))
# the program should print out a positive encouragement if one of these conditions are fullfilled and a negative encouragement if none of them are true
if Nr1 == Nr2 and Nr3 == Nr4:
    print("You are great!")

elif Nr1 == Nr3 and Nr2 == Nr4:
    print("You are great!!")

elif Nr1 == Nr4 or Nr2 == Nr3:
    print("You are great!!!")

else:
    print("Nope")

# oder
if (
    (Nr1 == Nr2 and Nr3 == Nr4)
    or (Nr1 == Nr3 and Nr2 == Nr4)
    or (Nr1 == Nr4 or Nr2 == Nr3)
):
    print("Yieha")

else:
    print("Nope")

# oder mit !=
if (
    (Nr1 != Nr3 and Nr1 != Nr4)
    or (Nr1 != Nr2 and Nr1 != Nr4)
    or (Nr1 != Nr2 and Nr1 != Nr3)
):
    print("You did it")
else:
    print("Sorry")

# oder mit if not
if not (Nr1 == Nr3 and Nr2 == Nr4):
    print("Looser")
else:
    print("Jackpot")
