"""
Exercise 16 - Simple dictionary
"""
TelNumbers = {}
TelNumbers["Kerstin"] = 24337763
TelNumbers["Agnes"] = 2390238
TelNumbers["Michi"] = 66592858
TelNumbers["Katrin"] = 63492120

print(TelNumbers)
NewName = input("What is your name: ")
New = int(input("What is your number: "))

TelNumbers[NewName] = New
print(TelNumbers)

OldName = input("Which name and number is not used anymore? Give the name: ")
del TelNumbers[OldName]
print(TelNumbers)
