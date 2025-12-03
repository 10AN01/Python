database = []

def menu():
    print("- - - Menu - - -")
    print("1)Add to list")
    print("2)Remove from list")
    print("3)View List")
    print("4)End Program")
    while True:
        choice = int(input("Enter a choice from 1-4: "))
        if choice == 1:
            add()
            break
        elif choice == 2:
            remove()
            break
        elif choice == 3:
            show()
            break
        elif choice == 4:
            print("You have no ended the program.")
            break

def add():
    print("You have chosen to add someone to the list.")
    while True:
        name = input("Enter person's name: ")
        break
    while True:
        age = input(f"Enter {name}'s age: ")
        #Error Handling
        try:
            age = int(age)
            break
        except ValueError:
            print("Invalid Age. Please Try Again.")
    #  Assigning variables to user's input
    # Adding users input to database
    data = {"name":name, "age":age}
    database.append(data)
    print(f"Added {name}'s as {age} years old, in the database.")
    again()
def remove():
    print("Working Progress")
def again():
    print("---------- Loop Menu -----------")
    print("Would you like to add another person?")
    print("1 = Yes")
    print("2 = No")
    while True:
        yesno = int(input("Enter from choice 1-2: "))
        if yesno == 1:
            add()
            break
        elif yesno == 2:
            menu()
            break
        else:
            print("Invalid Option.")
            
    
def show():
    print("- - - - Your Database - - - -")
    counter = 0 
    for data in database: # Loops until it's went through all the rows of data.
        counter += 1 #Adds one to counter everytime it loops.
        print(f"Person ", counter)
        print("Name: ",data["name"], "\nAge: ",data["age"]) # Prints data starting from the first
    while True:
        print("- - - - Exit Program Menu - - - -")
        print("1 - Yes")
        print("2 - No")
        exit = int(input("Would you like to exit the program? "))
        if exit == 1:
            print("You have exited the program")
            break
        elif exit == 2:
            menu()
            break
    

menu()