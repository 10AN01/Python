import json

datafile = []

def menu():
    print("| MENU |")
    print("1.Add animal")
    print("2.Remove animal")
    print("3.View animals stored")
    print("4.End Program")
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
            break
    

def program():
    while True:
        try:
            loops = int(input("How many animals will you like to add? "))
            break
        except ValueError:
            print("Invalid Number. Try Again.")
    counter = 0
    for i in range(loops):
        counter += 1
        print(f"- - - - - - - - {counter} animal - - - - - - - -")
        while True:
            name = input("Enter animals name: ")
            if name == "":
                print("Enter a name.")
            else:
                print("")
                break
        while True:
            try:
                age = int(input(f"Enter {name}'s age:  "))
                break
            except ValueError:
                print("Invalid Number. Try again.")
        while True:
            animal = input("Enter what animal: ")
            if animal == "":
                print("Enter a what animal")
            else:
                print("")
                break
        while True:
            breed = input("Enter pet breed: ")
            if breed == "":
                print("Enter a breed.")
            else:
                print("")
                break
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
    endprogram()
def view():
    with open("databasefile.json", "r") as f:
        animals = json.load(f)["Animal Data"]
        counter = 0
    for animal in animals:
        counter += 1
        print(f"- - - - {counter} - - - -")
        print("Name:", animal["name"],"|Age:", animal["age"],"|Animal:", animal["animal"],"|Breed:", animal["breed"])
        print()

def remove():
    with open("databasefile.json", "r") as f:
        animals = json.load(f)["Animal Data"]
        counter = 0
    for animal in animals:
        counter += 1
        print(f"- - - - {counter} - - - -")
        print("Name:", animal["name"],"|Age:", animal["age"],"|Animal:", animal["animal"],"|Breed:", animal["breed"])
        print()
      
    index_delete = int(input("Enter corrosponding number to data: "))
    #we do -1 as the first starts with 0
    index_delete = index_delete - 1
    #Shows what it's deleting
    print(animals[index_delete])
    del animals[index_delete]
        #Replace the list currently with the one in the json
    with open("databasefile.json", "w") as f:
        json.dump({"Animal Data": animals}, f, indent=4)
    menu()
    

def endprogram():
    print("Use Y(Yes) or N(No)")
    while True:
        end = input("End Program?  ").lower()
        if end == "y" or end == "yes":
            print("Goodbye!")
            break
        elif end == "n" or end == "no":
            menu()
            break
        else:
            print("Invalid Option. Try Again.")
    
    
    

menu()
        