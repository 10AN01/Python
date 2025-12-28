# - - - - - PLAN - - - - -
#1. Shows menu with options (Add product,Remove product, List products, End Program)
#2.When adding product should ask for name of product, price
#3.Remove product should just show a list and enter a number to remove it
#4. List product should show all the products stored.
import json
datalist = []

def menu():
    print("- - - - - MENU - - - - -")
    print("- - 1.Add Product(s) - -")
    print("- -2.Remove Product(s)- -")
    print("- - 3.Show Product(s) - -")
    print("- - - 4.End Program - - -")
    print("- - - - - - - - - - - - -")
    while True:
        choice = int(input("Enter a choice 1-4: "))
        if choice == 1:
            add_product()
        elif choice == 2:
            remove_product()
        elif choice == 3:
            show_product()
        elif choice == 4:
            end_program()
        else:
            print("Invalid option. Try again.")



def add_product():
    while True:
        try:
            loops = int(input("How many products will you like to add? "))
            break
        except ValueError:
            print("Invalid Number. Try Again.")
            break
    for i in range(loops):
        name_product = input("What is your product: ")
        while True:
            try:
                price_product = int(input("What is the price of your product? £"))
                break
            except ValueError:
                print("Invalid Number. Try Again.")
                break
        location_bought = input("Enter where the product was bought: ")
        datainputted = {"Product Name":name_product,"Price Of Product":price_product,"Location Bought":location_bought}
        datalist.append(datainputted)
    try:
        with open("databasefile.json", "r") as f:
            old_data = json.load(f)
            old_data = old_data["Products"]
            datalist.extend(old_data)
        with open("databasefile.json", "w") as f:
            json.dump({"Products":datalist},f, indent= 4)
            print("Sucessfully added data!")
    except FileNotFoundError:
        with open("databasefile.json", "w") as f:
            json.dump({"Products":datalist},f, indent= 4)
        
        
        
        
    
def remove_product():
    print("Working Progress")
def show_product():
    try:
        with open("databasefile.json", "r") as f:
            products_data = json.load(f)["Products"]
        print("- - All Products - -")
        for products in products_data:
            print(
                "Product:", datalist["name_product"],
                "Price £:", datalist["price_product"],
                "Store:", datalist["location_bought"]
            )
    except FileNotFoundError:
        print("You have no data. Taking back to menu.")
        menu()
def end_program():
    print("Working Progress")


menu()