import json

datafile = []

def menu():
    print("| MENU |")
    print("1.Add animal")
    print("2.Remove animal")
    print("3.View animals stored")
    while True:
        choices = int(input("Enter a choice: "))
        if choices == 1:
            program()
            break
        elif choices == 2:
            remove()
        elif choices == 3:
            view()
        elif choices == 4:
            endprogram()
    

def program():
    while True:
        try:
            loops = int(input("How many animals will you like to add?"))
            break
        except ValueError:
            print("Invalid Number. Try Again.")
    for i in range(loops):
        counter = 0
        counter += 1
        print(f"{counter} animal")
        name = input("Enter animals name: ")
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
        #Read file if exist.
        #assign the file as old data, add the old data to the new.
        with open ("databasefile.json", "r") as f:
            old_data = json.load(f)
            old_data = old_data["Animal Data"]
            datafile.extend(old_data)
        #Write the old + new data in the file with the category "Animal Data"
        with open ("databasefile.json", "w") as f:
            json.dump({"Animal Data":datafile},f , indent =4)
            print("Sucessfully added data!")
        #If file doesn't exist/is empty write the file with the category "Animal Data"
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

def endprogram():
    print("Use Y(Yes) or N(No)")
    while True:
        end = input("End Program?  ")
        if end.lower() == "Y" or  end.lower() == "yes":
            print("Goodbye!")
            break
        elif end.lower() == "N" or end.lower() == "no":
            program()
            break
        else:
            print("Invalid Option. Try Again.")
    
    
    

menu()
        