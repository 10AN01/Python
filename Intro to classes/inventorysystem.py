import json

def int_errorhandling(prompt):
    while True:
        try:
            return int(input(prompt))
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
                self.items_list.extend(exisitingdata["items_dict"])
#File not found just print
        except FileNotFoundError, json.JSONDecodeError:
            print("You have no existing data.")
    def addinventory(self):
        item = input("Enter a item you'll like to add:")
        price = int_errorhandling(f"Enter the cost of {item}: £")
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
        
        datainputted = ItemStuff(item,price,quantity,category)
        
        data_dic = {
            "Item: ":datainputted.item,
            "Price: ":datainputted.price,
            "Quantity: ":datainputted.quantity,
            "Category: ":datainputted.category,
            
        }
        self.item_list.append(data_dic)
        with open ("inventoryfile.json", "w") as f:
                json.dump(self.book)
            
class ItemStuff:
    def __init__(self,item,price,quantity,category):
        self.item = item
        self.price = price
        self.quantity = quantity
        self.category = category
            
        
inventorysystem = InventorySystem()
inventorysystem.addinventory()



    




