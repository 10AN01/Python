import json

datafile = []


def program():
    while True:
        try:
            loops = int(input("How many dogs will you like to add?"))
            break
        except ValueError:
            print("Invalid Number. Try Again.")
    for i in range(loops):
        name = input("Enter dogs name: ")
        while True:
            try:
                age = int(input(f"Enter {name}'s age:  "))
                break
            except ValueError:
                print("Invalid Number. Try again.")
        animal = input("Enter what animal: ")
        breed = input("Enter pet breed: ")
        datainput = {"name":name, "age":age,"animal":animal, "breed":breed}
        datafile.append(datainput)
    try:
        with open ("databasefile.json", "r") as f:
            old_data = json.load(f)
            old_data = old_data["Animal Data"]
            datafile.extend(old_data)
        with open ("databasefile.json", "w") as f:
            json.dump({"Animal Data":datafile},f , indent =4)
            print("Sucessfully added data!")
    except (FileNotFoundError, json.JSONDecodeError):
        with open ("databasefile.json", "w") as f:
            json.dump({"Animal Data":datafile},f , indent =4)
            print("Json file not found. Created json file.")
def view():
    with open("databasefile.json", "r") as f:
        animals = json.load(f)["Animal Data"]

    for animal in animals:
        counter = 0
        counter += 1
        print(f"- - - - {counter} - - - -")
        print("Name:", animal["name"])
        print("Age:", animal["age"])
        print("Animal:", animal["animal"])
        print("Breed:", animal["breed"])
        print()
menu()
        