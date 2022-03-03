"""
Exercise 19 - Adjusting the address book
"""
# copy addressbool from Exercise 18
# keep in mind, to check if the user is giving an usable input
addressbook = {}
addressbook["Mia"] = {}
addressbook["Mia"]["City"] = "Karlsruhe"
addressbook["Mia"]["Number"] = 1
addressbook["Mia"]["Birthday"] = "Feb"
addressbook["Mia"]["Email"] = "none"
addressbook["Gudrun"] = {}
addressbook["Gudrun"]["City"] = "Rinklingen"
addressbook["Gudrun"]["Number"] = 2
addressbook["Gudrun"]["Birthday"] = "Aug"
addressbook["Gudrun"]["Email"] = "Gud"
addressbook["Markus"] = {}
addressbook["Markus"]["City"] = "Karlsruhe"
addressbook["Markus"]["Number"] = 3
addressbook["Markus"]["Birthday"] = "Sep"
addressbook["Markus"]["Email"] = "Mdolch"
addressbook["Joachim"] = {}
addressbook["Joachim"]["City"] = "Schwabach"
addressbook["Joachim"]["Number"] = 4
addressbook["Joachim"]["Birthday"] = "Nov"
addressbook["Joachim"]["Email"] = "Jo"
addressbook["Simone"] = {}
addressbook["Simone"]["City"] = "Bamberg"
addressbook["Simone"]["Number"] = 5
addressbook["Simone"]["Birthday"] = "Apr"
addressbook["Simone"]["Email"] = "SiNi"
addressbook["Cecilia"] = {}
addressbook["Cecilia"]["City"] = "Berlin"
addressbook["Cecilia"]["Number"] = 6
addressbook["Cecilia"]["Birthday"] = "Jul"
addressbook["Cecilia"]["Email"] = "Ceci"
print(addressbook)
# asking for: adding, deleting or changing an entry
change1 = input("Do you want to add, delete or change an entry: yes or no: ")
# if user wants to delete, ask again which entry and delete it
if change1 == "yes":
    change2 = input("Do you want to delete an entry: yes or no: ")
    if change2 == "yes":
        delete1 = input("Which Name do you want to delete: ")
        if change2 not in addressbook:
            print("No such entry")
        else:
            del addressbook[delete1]
# if user wants to change, ask gain which entry and to what it should be changed and change it
change3 = input("Do you want to change an entry: yes or no: ")
if change3 == "yes":
    change4 = input("Which part do you want to change: City, Number, Birthday, Email: ")
    if change4 == "Number":
        name = input("Of which person do you want to change the number: ")
        if name not in addressbook:
            print("Wrong input")
        else:
            number = input("What is the new number: ")
            addressbook[name]["Number"] = number
    elif change4 == "City":
        name1 = input("Of which person do you want to change the city: ")
        if name1 not in addressbook:
            print("Wrong input")
        else:
            city = input("What is the new city: ")
            addressbook[name1]["City"] = city
    elif change4 == "Birthday":
        name2 = input("Of which person do you want to change the birthday: ")
        if name2 not in addressbook:
            print("Wrong input")
        else:
            birthday = input("What is the new birthday: ")
            addressbook[name2]["Birthday"] = birthday
    elif change4 == "Email":
        name3 = input("Of which person do you want to change the Email: ")
        if name3 not in addressbook:
            print("Wrong input")
        else:
            email = input("What is the new Email: ")
            addressbook[name3]["Email"] = email
    else:
        print("No such entry")
# if user wants to add an entry, ask for all informations and create it
change5 = input("Do you want to add an entry: yes or no: ")
if change5 == "yes":
    name4 = input("What is the name: ")
    if name4 not in addressbook:
        city2 = input("In which city does " + name4 + " lives: ")
        number2 = input("What's " + name4 + "'s number' : ")
        birthday2 = input("When is " + name4 + "'s birthday: ")
        email2 = input("What's " + name4 + "'s email: ")
        addressbook[name4] = {}
        addressbook[name4]["City"] = city2
        addressbook[name4]["Number"] = number2
        addressbook[name4]["Birthday"] = birthday2
        addressbook[name4]["Email"] = email2
        # or
        # addressbook[name4] = {"City": city2, "Number": number2, "Birthday": birthday2, "Email": email2}
    else:
        input("This already exists")
print(addressbook)
