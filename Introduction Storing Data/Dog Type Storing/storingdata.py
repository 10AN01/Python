import json
import os
database = []

def menu():
    print("|/\/\/\/\/\/\/\/\/\/\/\/\/|")
    print("|          MENU           |")
    print("|/\/\/\/\/\/\/\/\/\/\/\/\/|")
    print("|  1.Add a person to list |")
    print("|2.Remove person from list|")
    print("|  3.View people in list  |")
    print("|      4. End Program     |")
    
    while True:
        choice = int(input("Enter a choice from 1-4: "))
        if choice == 1:
            add()
        elif choice == 2:
            remove()
        elif choice == 3:
            view()
        elif choice == 4:
            print("You have exited the program.")
            break
        else:
            print("Invalid Option")
                


def add():
    while True:
        loop = int(input("How many people will you like to add? "))
        print(f"You have chosen to add {loop} people")
        print("NOTE! Add one name no spaces!")
        for i in range(loop):
        # Loops however many types user inputed the loop
            while True:
                name = input("Enter the persons name: ")
                # Error Handling
                if name.isalpha():
                    print("Added name")
                    break
                else:
                    print("Invalid name. Must have NO spaces & numbers")
            while True:
                age = input("Enter the person's age: ")
                # Error Handling (If user is a number carry on)
                try:
                    age == int(age)
                    print("Valid Age")
                    break
                except ValueError:
                    print("Invalid Age. Please enter a number")
            while True:
                gender = input("Type are you male or female: ").lower()

                # Error Handling (Only accepted male or female)
                if gender == "male".lower():
                    print("You have chosen male")
                    print(f"Have added {name} who is a {gender} and is {age} years old.")
                    break
                elif gender == "female".lower():
                    print("You have chosen female")
                    print(f"Have added {name} who is a {gender} and is {age} years old.")
                    break
                else:
                    print("Invalid Option. Please pick male or female.")
            # Assigning inputs to variable.
            data = {"name": name, "age": age, "gender": gender}
            # Storing data in the json file
            database.append(data)

            #REDO EVERYTHING UNDERHERE
            try:
                if os.path.getsize ("database.json") >=0: #Is file is greater or equal to 0
                    with open ("datafile.json", "r") as f: #read file
                        existing = json.load(f) # loads the old data
                        existing.extend(database) # adds old data to the list.
            except FileNotFoundError:
                existing = database # assigns the empty file to the layout.
                with open("datafile.json", "w") as f:
                    json.dump(existing,f , indent = 4)
        break
    menu()

    



def remove():
    try:
        with open ("datafile.json", "r") as f:
            load = json.load(f)
            username = input("Who would you like to remove from the file? ")
            if username = load[name]:
                load.remove(username)
    except ValueError:
        print ("No data found!")
    except json.JSONDecodeError:
        print ("No data found!")
def view():
    try:
        with open ("datafile.json", "r") as f:
            info = json.load(f)
            print("- - - - User Info - - - -")
            counter = 0
            for person in info:
                counter += 1 # adds one to the counter
                print(f"- - - - - Person {counter} - - - - -")
                print(f"Name: {person['name']}")
                print(f"Age: {person['age']}")
                print(f"Gender: {person['gender']}")
    except FileNotFoundError:
        print("No data Found. Try adding some data.")
    except json.JSONDecodeError:
        print("No data Found. Try adding some data.")
menu()