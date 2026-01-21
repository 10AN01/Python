import json
def menu():
    print("MENU")
    print("1.Add Items")
    print("2.Remove Items")
    print("3.View items")
    print("4.End Program")
    while True:
        choice = int(input("Enter a choice from 1-4: "))
        if choice == 1:
            inventorysystem.addinventory()
            break
        elif choice == 2:
            inventorysystem.deleteinventory()
            break
        elif choice == 3:
            inventorysystem.view_database()
            break
        elif choice == 4:
            inventorysystem.end_program()
            break
        else:
            print("Invalid Number")
        
    
def int_errorhandling(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Use Number")
def float_errorhandling(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Use Number")
class InventorySystem:
    def __init__(self):
        self.items_list = []
# Reads the exisitng file
# Adds existing data to the list.
        try:
            with open ("inventoryfile.json", "r") as f:
                exisitingdata = json.load(f)
                self.items_list.extend(exisitingdata["item_dict"])
#File not found just print
        except FileNotFoundError, json.JSONDecodeError:
            print("You have no existing data.")
#ADDING ITEMS FUNCTION
    def addinventory(self):
#User inputs there data.
        item = input("Enter a item you'll like to add:")
        price = float_errorhandling(f"Enter the cost of {item}: £")
        quantity = int_errorhandling(f"Enter a quantity of {item}: ")
        print("====================================")
        print("          ITEM CATEGORIES")
        print("====================================")
        print("  [1] Consumable")
        print("  [2] Equipment")
        print("  [3] Material")
        print("  [4] Media")
        print("  [5] Clothing")
        print("  [6] Miscellaneous")
        print("====================================")

        category_input = int(input("Enter the category (1-4): "))
        category = ""
        while True:
            if category_input == 1:
                category = "Consumable"
                break 
            elif category_input == 2:
                category = "Equipment"
                break 
            elif category_input == 3:
                category = "Material"
                break 
            elif category_input == 4:
                category = "Media"
                break 
            elif category_input == 5:
                category = "Clothing"
                break 
            elif category_input == 6:
                category = "Miscellaneous" 
                break 
            else:
                print("Invalid Category. Try Again.")
#Collects data and formats it       
        datainputted = ItemStuff(item,price,quantity,category)
        
        data_dic = {
            "Item:":datainputted.item,
            "Price:":datainputted.price,
            "Quantity:":datainputted.quantity,
            "Category:":datainputted.category,
            
        }
#Adds the format to the list: Updates it so the file.
        self.items_list.append(data_dic)
        with open ("inventoryfile.json", "w") as f:
                json.dump({"item_dict":self.items_list}, f, indent=4)
                
# DELETING ITEMS FUNCTION                
    def deleteinventory(self):
        counter = 0
#No data in list print
        if not self.items_list:
            print("No items to delete.")
            return
# Will keep looping depending on how much data there is
        for items in self.items_list:
            counter += 1
            print(f"= = = = = Item {counter} = = = = = ")
            print(f"Item: {items['Item:']}")
            print(f"Price: £{items['Price:']}")
            print(f"Quantity: {items['Quantity:']}")
            print(f"Category: {items['Category:']}")
        while True:
# Deleting feature
# Takes away 1 from the choice because of the index
            Item_Choice = int(input("Enter the item number you would like to remove: "))
            index = Item_Choice - 1

            if 0 <= index < len(self.items_list):
#Remove item from list.
                self.items_list.pop(index)
                print("Item removed.")
#Update it in the file
                with open("inventoryfile.json", "w") as f:
                    json.dump({"item_dict": self.items_list}, f, indent=4)

                break
            else:
                print("Invalid.")
        
    def view_database(self):
        print("= = = = = = = = = = = = = =")
        for items in self.items_list:
               print(f"Item: {items['Item:']}")
               print(f"Price: £{items['Price:']}")
               print(f"Quantity: {items['Quantity:']}")
               print(f"Category: {items['Category:']}")
               print("-" * 30)
    
    def end_program():
        print("Bye bye!")
            
class ItemStuff:
    def __init__(self,item,price,quantity,category):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.category = category
            
        
inventorysystem = InventorySystem()

menu()



    




