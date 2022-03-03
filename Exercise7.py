"""
Exercise 7 - Other comparisons
"""
# take the program from Exercise 6 and add some more statements for printing out a positive encouragement
Nr1 = int(input("Give me one number: "))
Nr2 = int(input("Give me another one: "))
Nr3 = int(input("and one more: "))
Nr4 = int(input("and a last one: "))

if Nr1 > Nr2 and Nr3 > Nr4:
    print("You are great!")

elif Nr1 < Nr3 and Nr2 < Nr4:
    print("You are great!!")

elif Nr1 == Nr4 or Nr2 >= Nr3:
    print("You are great!!!")

elif Nr1 <= Nr4 and Nr2 == Nr3:
    print("You are great!!!!")

else:
    print("Nope")

if Nr1 == Nr2 == Nr3 == Nr4:
    print("Jackpot")

elif Nr1 != Nr2 and Nr1 != Nr3 and Nr1 != Nr4:
    print("Looser")

else:
    print("as always")
