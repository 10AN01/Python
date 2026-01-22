
data = {
    "income": 0,
    "source_of_income": "",
    "expenses": [],
    "expenses_on": [],
}

def menu():
    print("\n============================")
    print("    💰 BudgetApp Menu 💰     ")
    print("============================")
    print("1. ➕ Add Income")
    print("2. ➖ Add Expenses")
    print("3. 💵 View Balance")
    print("4. 💾 Save & Exit")
    print("============================")
    while True:
        #choices#
        choice = int(input("Enter a choice you'll like to do: "))
        if choice == 1:
            income()
        elif choice == 2:
            expenses_menu()
        elif choice == 3:
            balance()
        elif choice == 4:
            print("You have exited the program.")
            break
        else:
            print("Invalid option.")
def income():
    print("You have chosen to add an income.")
    while True:
        try:
            incomemoney = int(input("Enter your income: "))
            data["income"] += incomemoney #adds user input to income
            while True:
                incomesource = str(input("Enter where the income came from: ")) #Enter Income
                if incomesource.isalpha():
                    data["source_of_income"] = incomesource #Assigns input to the varible in the dictonary
                    print("You have added",incomemoney ,"to your income from",incomesource)
                    menu()
                    break
                else:
                    print("Invalid source")
        except ValueError:
            print("Please enter a valid number for the income.")


def expenses_menu():
    print("You have chosen to add your expenses")
    print("\n============================")
    print("      💰 Expenses Menu 💰     ")
    print("============================")
    print("1. ➕ Add seperately")
    print("2. ➕ Add all together")
    print("3. 💾 Save & Exit")
    expenses_choice = int(input("Enter your choice: "))
    if expenses_choice == 1:
        print("You have chosen to add seperately")
        while True:
            try:
                loops = int(input("How many items will you like to add? "))
                expense_seperate(loops)
            except ValueError:
                print("Invalid Number")
    elif expenses_choice == 2:
        print("You have chosen to add the full amount")
        while True:
            try:
                full_amount = int(input("Enter how much you've spent in total: "))
                data["expenses"].append(full_amount) # adds users input to expenses
                while True:
                    expense_source = input("Enter the source of the expense: ")
                    if expense_source.isalpha(): #meaning a stri or has no spaces
                        print("You have added £",full_amount,"on",expense_source)
                        data["expenses_on"].append(expense_source) #add input to expenses_on
                        menu()
                        break
                    else:
                        print("Invalid Source")
            except ValueError:
                print("Invalid Number")

        
def expense_seperate(loops):
    for i in range(loops): #loops depending what user inputted
        while True:
            try:
                print("You have chosen to add",loops,"expenses seperately.")
                expense_money = int(input("Enter how much the amount expense is: "))
                while True:
                        expense_source = input("Enter the source of the expense: ")
                        if expense_source.isalpha():
                            print("You have added £",expense_money,"to your",expense_source)
                            #adds inputs of user to data
                            data["expenses"].append(expense_money)
                            data["expenses_on"].append(expense_source)
                            break
                        else:
                            print("Invalid Source")

                break
            except ValueError:
                print("Invalid Number")
    menu()


def balance():
    balancetotal = data["income"] - sum(data["expenses"]) #finds how much money is left
    print("Income:","£",data["income"],"|","Source:",data["source_of_income"]) #Prints the data
    print("-------------------------------------------------")
    for i in range(len(data["expenses"])): #prints depending on how many expenses there are in the list
        print("Expenses: £", data["expenses"][i], "| Source:", data["expenses_on"][i])

    print("Expenses Total:","£",sum(data["expenses"]))
    print("-------------------------------------------------")
    if balancetotal >= 0:
        print("Total Balance:","✅£",balancetotal)
        print("You're in the positives")
    elif balancetotal < 0:
        print("Total Balance:","❌£",balancetotal)
        print("You're in the negatives")


menu()