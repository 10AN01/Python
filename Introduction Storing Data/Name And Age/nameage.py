import json
userlist = []
def program():
    print("You can add anyone to the database!")
    while True:
        try:
            loop = int(input("How many people will you like to add?  "))
        except ValueError:
            print("Invalid number.Try again")
        break
    for i in range(loop):
        name = input("Input person's name: ")
            #if user doesn't enter a integer print Invalid option.
        while True:
            try:
                age = int(input(f"Input {name}'s age: "))
                break
            except ValueError:
                print("Invalid Option")
            # If gender is a female/male print else print invalid option.
        while True:
                #if input does not equal to Male or Female print Invalid Option.
            gender = input("Male or female? ")
            if gender.lower() == "male" or gender.lower() == "female":
                print(f"{name} is a {gender}")
                break
            else:
                print("Invalid Option")
            # Assigned a format. add the data inputted by user to the list.
        datainputted = {"name":name, "age":age,"gender":gender}
        userlist.append(datainputted)
        print("Data has been inputted:")
        try:
            with open ("database.json", "r") as f:
                old_data = json.load(f)
                old_data = old_data["user"]
                userlist.extend(old_data)
                    
            with open ("database.json", "w") as f:
                json.dump({"user": userlist}, f, indent=4)          
                break
        except FileNotFoundError:
            with open ("database.json", "w") as f:
                json.dump({"user": userlist}, f, indent=4)                   
                break
def end():
    print("------------End Program Menu------------")
    print("1. Carry on")
    print("2. End program")
    while True:
        userinput = int(input("Would you like to end the program?"))
        if userinput == 1:
            program()
        elif userinput == 2:
            print("Goodbye!")
            break
        else:
            print("Invalid Option.")
        
program()