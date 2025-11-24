import json
import os
petdata = {
    "petname": [],
     "type": [],
     "age": [],
}


def menu():
    print("|------------------------------|")
    print("|          PET STORING         |")
    print("|/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|")
    print("|         1.Add a pet          |")
    print("|       2.Search a pet up      |")
    print("|        3.View all pets       |")
    print("|        4.Quit program        |")
    print("|------------------------------|")
    while  True:
        choice = int(input("Enter a choice from 1-4: "))
        if choice == 1:
            addpet()
        elif choice == 2:
            searchpet()
        elif choice == 3:
            viewall()
        elif choice == 4:
            print("You have ended the program")
            break
        else:
            print("You have picked an invalid option")

def addpet():
    print("You have chosen to add a pet!")
    while True:
        try:
            loops = int(input("How many pets would you like to add? "))
            print("You have chosen to add",loops,"pets.")
            for i in range(loops):
                name = input("Enter your pet name: ")
                if name.isalpha():
                    petdata["petname"].append(name)
                    print("Name has been added!")
                else:
                    print("Use Letters Only!")
                type = input("Enter the pet type: ")
                petdata["type"].append(type)
                if type.isalpha():
                    print("Pet type has been added!")
                else:
                    print("Use Letters Only!")
                try:
                    age = int(input("Enter your pet's age: "))
                    petdata["age"].append(age)
                    print("Age has been added!")
                except ValueError:
                    print("Invalid age")
        except ValueError:
            print("Enter a number not letters")
        break
def searchpet():
    print("weee")
def viewall():
    counter = 0
    print("NAME ---- TYPE ---- YEARS OLD")
    for i in (petdata["petname"]):
        counter += 1
        print("pet",counter)
        print("- - - - - - - - - - - - - - - -")
        print(petdata["petname"][i],petdata["type"][i],petdata["age"][i])

menu()