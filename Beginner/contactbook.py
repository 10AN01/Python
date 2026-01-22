
contacts= [
]


def menu():
    print("----------------------------")
    print("|---Contact Book Program---|")
    print("|-----1.Add a contacts-----|")
    print("|-----2.View contacts------|")
    print("|----3.Search contacts-----|")
    print("|----4.Delete contacts-----|")
    print("|----------5.Exit----------|")
    print("----------------------------")
    while True:
            try:
                choice = int(input("What would you like to do? "))
                if choice == 1:
                    add()
                elif choice == 2:
                    view()
                elif choice == 3:
                    search()
                elif choice == 4:
                    delete()
                elif choice == 5:
                    print("You have exited the program.")
                    break
                else:
                    print("Invalid option")
            except ValueError:
                 print("Invalid option")
def add():
    while True: #if statement is true
        try: #It tries this. If there is no integer it will loop.
            print("You have chosen to add a contact")
            many = int(input("How many contacts will u like to add? "))
            print("You have chosen to add",many, "contacts")
            break
        except ValueError: #/= int (giving a value error) will print Invalid number
            print("Invalid number")
    
    for i in range(many):
        name = input("Enter your contact's name: ")
        number = input("Enter your contact's number: ")
        try:
            int(number)
            if len(number) == 11:
                print("You have successfully added", name, "as a contact")
                contact = {"name":name,"phone number":number} #format in list
                contacts.append(contact) # adds contact to list contacts
            else:
                print("Number must be 11 digits")
        except ValueError:
            print("Invalid Number")

    print(contacts)
def search():
    name_search = input("Enter a contact you'll like to search: ")
    for contact in contacts:
        if contact["name"].lower() == name_search.lower():
            print("Found contact!")
            print("Name:",contact["name"])
            print("Phone Number",contact["phone number"])
        elif contact["name"].lower() != name_search.lower():
            print("Contact not found")
        else:
            ("Contact not found.")
def delete():
    print("When you're finish type the word done")
    while True:
        name_delete = input("Enter a contact you'll like to remove: ")
        if name_delete.lower() == "done":
            break
        try:
            for contact in contacts: #loops depending on how many contacts there are
                if contact["name"] == name_delete:
                    contacts.remove(contact)
                    print(contact, "found and removed!")
        except ValueError:
            print("Invalid contact in list. Try again.")
def view():
    print(contacts)

menu()

