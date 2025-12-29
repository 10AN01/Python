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
        try:
            choice = int(input("Enter a choice 1-4: "))
            if choice == 1:
                add_product()
                break
            elif choice == 2:
                remove_product()
                break
            elif choice == 3:
                show_product()
                break
            elif choice == 4:
                end_program()
                break
            else:
                print("Invalid option. Try again.")
                break
        except ValueError:
            print("Invalid Option")



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
        #Assigning format & adding data to the datalist
        datainputted = {"Product Name":name_product,"Price Of Product":price_product,"Location Bought":location_bought}
        datalist.append(datainputted)
        
        #Read the file & add old data to the new data
        #Then write everything in the datalist (both old & new) into the databasefile.json file.
    try:
        with open("databasefile.json", "r") as f:
            old_data = json.load(f)
            old_data = old_data["Products"]
            datalist.extend(old_data)
        with open("databasefile.json", "w") as f:
            json.dump({"Products":datalist},f, indent= 4)
            print("Sucessfully added data!")
            end_program()
        
        #If the file doesn't exist or is empty, dump the datalist.
    except FileNotFoundError, json.JSONDecodeError:
        with open("databasefile.json", "w") as f:
            json.dump({"Products":datalist},f, indent= 4)
            end_program()
        
        
        
        
    
def remove_product():
    print("You have selected to remove a product")
    #Read the database.json file in order to print the data information
    with open("databasefile.json", "r") as f:
            products_data = json.load(f)["Products"]
    print("- - All Products - -")
    counter = 0
    for products in products_data:  
        counter += 1    
        print(f"{counter} Product(s)")      
        print(
            "Product:", products["Product Name"],
            "| Price £", products["Price Of Product"],
            "| Store:", products["Location Bought"]
            )
        # Read file, enter what you'll like to delete
        # Remove selected from the datalist.
        # Write whatever is in the list currently into the databasefile.json
    with open("databasefile.json", "r") as f:
        datalist = json.load(f)["Products"]

    delete_product = int(input("Enter a number of product you'll like to delete: "))
    true_delete_product = delete_product - 1
    del datalist[true_delete_product]
    try:
        with open("databasefile.json", "w") as f:
            json.dump({"Products":datalist},f, indent= 4)
            print("You have successfully deleted .")
        # If file doesn't exist or is empty print message
    except FileNotFoundError, json.JSONDecodeError:
        print("Json doesn't exist or has nothing in it.")
        end_program()
def show_product():
    try:
        with open("databasefile.json", "r") as f:
            products_data = json.load(f)["Products"]
        print("- - All Products - -")
        for products in products_data:
            print(
            "Product:", products["Product Name"],
            "| Price £", products["Price Of Product"],
            "| Store:", products["Location Bought"]
            )
            print("= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =")
        end_program()
    except FileNotFoundError:
        print("You have no data. Taking back to menu.")
        menu()
def end_program():
    while True:
        print("Answer only yes or no")
        end_question = input("End Program? ")
        if end_question.lower() == "yes":
            print("Goodbye")
            break
        elif end_question.lower() == "no":
            menu()
            break
        else:
            print("Invalid Option")
        



menu()