#Adding accounts (like a new bank account)
#Viewing accounts
#Delete accounts


 # - - - - Extra - - - -
 # Interact with different accounts
# Depositing and withdrawing money
# View transaction history

import csv
from errorhandle import int_errorhandling,float_errorhandling,str_errorhandling,email_errorhandling
from main import menu
class BankingSystem:
    def __init__(self):
#Sets the lists at the start of the code.
        self.account_list = []
        try:
# Adds old data to the list
            with open("bankinginformation.csv","r") as f:
                readcsv = csv.DictReader(f)
                self.account_list.extend(readcsv)
        except FileNotFoundError:
            self.account_list = [] 
# = = = = = = = ADD ACCOUNT  = = = = = = = 
    def add_account(self):
        balance = 0
#Users inputs
        print("You have chosen to add an account.")
        firstname = str_errorhandling("Enter your first name: ")
        lastname =  str_errorhandling("Enter your last name: ")
        email = email_errorhandling("Enter your email: ")
        while True:
            password = input("Input your password: ")
            password_confirm = input("Input password again: ")
            if len(password) > 4 and password == password_confirm:
                break
            else:
                print("Password to weak or doesn't match.")
        transaction =""
        datainputted = BankInformation(firstname,lastname,email,password,balance)
#Takes first 3 of the user name & lastname and puts them together to make a custom username
        custom_username = firstname[:3] + lastname[:5]
        print(f"Your username has been set to {custom_username}")
        print("=" * 30)
        print("Deposit Menu               ")
        print("=" * 30)
        print("1)Deposit")
        print("2)Leave deposit as 0")
        deposit_choice = int(input("Enter from options 1-2: "))
        while True:
            if deposit_choice == 1:
                new_balance = float_errorhandling(f"Enter the amount you'll like to deposit into {custom_username}: £")
                balance = new_balance
                break
            elif deposit_choice == 2:
                break
        transaction = (f"{custom_username} || User added {firstname} {lastname} to banking system.")
        
#Set the layout in dictonary layout in the list
#Adds the data to the list
        datadict = {
            "First Name":firstname,
            "Last Name":lastname,
            "Username":custom_username,
            "Email":email,
            "Password":password,
            "Account Balance":balance,
            "Transaction":transaction
        }
        datainputted.transcation.append(transaction)
        self.account_list.append(datadict)
#Writes headers/title in the file and writes all data onto the file
        with open("bankinginformation.csv","w",newline="") as f:
            fieldnames = ["First Name","Last Name","Username","Email","Password","Account Balance","Transaction"]
            writecsv = csv.DictWriter(f,fieldnames=fieldnames)
            writecsv.writeheader()
            writecsv.writerows(self.account_list)
# = = = = = = = = REMOVE ACCOUNT = = = = = = = = 
    def remove_account(self):
        print("You have chosen to remove an account.")
        if len(self.account_list) == 0:
            print("No Accounts In Database.")
            menu()
        counter = 0
        for accounts in self.account_list:
            counter += 1
            print(f"Account {counter}")
            print(f"= = {accounts["Username"]} = =")
            print(f"First Name: {accounts["First Name"]}")
            print(f"Last Name: {accounts["Last Name"]}")
            print(f"Email: {accounts["Email"]}")
        while True:
# Checks for first name in database
            ask_firstname = input("First name of account: ")
            for accounts in self.account_list:
                if ask_firstname == accounts["First Name"]:
                    break
                else:
                    print(f"Invalid user name {ask_firstname}")
                    retry = input("Try again? (y/n): ")
                    if retry.lower() == "y":
                        bankingsystem.remove_account()
                        break
                    elif retry.lower() == "n":
                        menu()
# Checks for last name in database.
            ask_secondname = input("Last name of account: ")
            for accounts in self.account_list:
                if ask_secondname == accounts["Last Name"]:
                    break
                else:
                    print(f"Invalid user name {ask_secondname}")
                    retry = input("Try again? (y/n): ")
                    if retry.lower() == "y":
                        bankingsystem.remove_account()
                        break
                    elif retry.lower() == "n":
                        menu()
                    break
# Checks if both names match
            for acounts in self.account_list:
                if ask_firstname == accounts["First Name"] and ask_secondname == accounts["Last Name"]:
                    print("Valid Account in system")
                    del accounts["First Name"]
                    with open ("bankinginformation.csv","w",lines="") as f:
                        fieldnames = ["First Name","Last Name","Username","Email","Password","Account Balance","Transaction"]
                        writecsv = csv.DictWriter(f,fieldnames=fieldnames)
                        writecsv.writeheader(f)
                        writecsv.writerows
                        break
                else:
                    print("Account first and last name doen't match.")
                    retry = input("Try again? (y/n): ")
                    if retry.lower() == "y":
                        bankingsystem.remove_account()
                        break
                    elif retry.lower() == "n":
                        menu()
                    break
    def view_account(self):
        for accounts in self.account_list:
            print("=" *15)
            print("ACCOUNT")
            print(f"{"Username"}")
            print("=" *15)
            print(f"First Name: {"First Name"}")
            print(f"Last Name: {"Last Name"}")
            print(f"Email: {"Email"}")
            
                


class BankInformation():
    def __init__(self,firstname,lastname,email,password,balance):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.balance = balance
        self.transcation = []
        
bankingsystem = BankingSystem()    