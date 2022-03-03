"""
Exercise 16 - Simple dictionary
"""
# write a program that generates a simple dictionary consisting of at least three pre defined entries
TelNumbers = {}
TelNumbers["Kerstin"] = 24337763
TelNumbers["Agnes"] = 2390238
TelNumbers["Michi"] = 66592858
TelNumbers["Katrin"] = 63492120

print(TelNumbers)
# ask the user for a new entry and add this new one to the dictionary afterwards
NewName = input("What is your name: ")
New = int(input("What is your number: "))

TelNumbers[NewName] = New
print(TelNumbers)

# then ask the user for an entry that should be removed and remove the entry from the dictionary
OldName = input("Which name and number is not used anymore? Give the name: ")
del TelNumbers[OldName]

# print out the remaining dictionary
print(TelNumbers)
