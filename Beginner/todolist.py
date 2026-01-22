task =[]

def menu():
    print("|----------------------------|")
    print("|-What would you like to do?-|")
    print("1.Add to list")
    print("2.Remove from list")
    print("3.Show list")
    print("4.End Program")
    while True:
        choice = int(input("What choice will you like to do? "))
        if choice == 1:
            add()
        elif choice == 2:
            remove()
        elif choice == 3:
            show()
        elif choice == 4:
            end()
        else:
            print("Pick a choice from the options")

def add():
    while True:
        print("Type done when you're finished")
        list = input("Enter what you'll like in your list: ")
        task.append(list)
        print("You have added",list, "to list")
        if list == "done":
            menu()
def remove():
    while True:
        print("Type done when you're finished")
        list = input("Enter what you'd like to remove: ")
        if list not in task:
            print("Your word is not in the list. Try again")
        if list in task:
            task.remove(list)
            print("You have removed",list, "from the list")
        if list == "done":
            menu()
def show():
    print("Your list:",task)
    menu()
def end():
    print("You have ended the program break")
menu()
