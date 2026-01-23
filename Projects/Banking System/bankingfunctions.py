# Adding accounts
# Viewing accounts
# Delete accounts 
# Interact with different accounts
# Depositing and withdrawing money
# View transaction history
import json
import csv
from errorhandle import int_errorhandling,float_errorhandling,str_errorhandling,email_errorhandling
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
            return
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
            found_first = False
            for accounts in self.account_list:
                if ask_firstname.lower() == accounts["First Name"].lower():
                    found_first = True
                    break
            if found_first == False:
                print(f"Invalid user name {ask_firstname}")
                retry = input("Try again? (y/n): ")
                if retry.lower() == "y":
                    bankingsystem.remove_account()
                    break
                elif retry.lower() == "n":
                    return
# Checks for last name in database.
            ask_secondname = input("Last name of account: ")
            found_last = False
            for accounts in self.account_list:
                if ask_secondname.lower() == accounts["Last Name"].lower():
                    found_last = True
                    break
            if found_last == False:
                print(f"Invalid last name {ask_secondname}")
                retry = input("Try again? (y/n): ")
                if retry.lower() == "y":
                    bankingsystem.remove_account()
                    break
                elif retry.lower() == "n":
                    return
# Checks if both names match
            found_both_names = False
            for accounts in self.account_list:
                if ask_firstname.lower() == accounts["First Name"].lower() and ask_secondname.lower() == accounts["Last Name"].lower():
                    print("Valid Account in system")
                    selected_account = accounts
                    found_both_names = True
            
            if found_both_names == True:
# Only allowed 3 attempts
                retry = 0
                
                password_found = False
                while True:
                    retry += 1
                    print("You only have 3 tries.")
                    print(f"You are on your {retry}/3 try")
                    if retry > 3:
                        return
                    password = input(f"Enter password for {ask_firstname} {ask_secondname}: ")
                    
                    if password == selected_account["Password"]:
                        password_found = True
                        break
                if password_found == True:
                    self.account_list.remove(selected_account)
                    with open ("bankinginformation.csv","w",newline="") as f:
                        fieldnames = ["First Name","Last Name","Username","Email","Password","Account Balance","Transaction"]
                        writecsv = csv.DictWriter(f,fieldnames=fieldnames)
                        writecsv.writeheader()
                        writecsv.writerows(self.account_list)
                        return
                if password_found == False:
                    continue
                        
            if found_both_names == False:
                print("Account first and last name doen't match.")
                retry = input("Try again? (y/n): ")
                if retry.lower() == "y":
                    bankingsystem.remove_account()
                    break
                elif retry.lower() == "n":
                    return
# Checks if they're the owner of account
    def view_account(self):
        for accounts in self.account_list:
            print("=" *15)
            print("ACCOUNT")
            print(f"{accounts["Username"]}")
            print("-" *15)
            print(f"First Name: {accounts["First Name"]}")
            print(f"Last Name: {accounts["Last Name"]}")
            print(f"Email: {accounts["Email"]}")

    def deposit_withdraw_account(self):
        if len(self.account_list) == 0:
            print("No Accounts In Database.")
            return
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
            found_first = False
            for accounts in self.account_list:
                if ask_firstname.lower() == accounts["First Name"].lower():
                    found_first = True
                    break
            if found_first == False:
                print(f"Invalid user name {ask_firstname}")
                retry = input("Try again? (y/n): ")
                if retry.lower() == "y":
                    bankingsystem.remove_account()
                    break
                elif retry.lower() == "n":
                    return
# Checks for last name in database.
            ask_secondname = input("Last name of account: ")
            found_last = False
            for accounts in self.account_list:
                if ask_secondname.lower() == accounts["Last Name"].lower():
                    found_last = True
                    break
            if found_last == False:
                print(f"Invalid last name {ask_secondname}")
                retry = input("Try again? (y/n): ")
                if retry.lower() == "y":
                    bankingsystem.remove_account()
                    break
                elif retry.lower() == "n":
                    return
# Checks if both names match
            found_both_names = False
            for accounts in self.account_list:
                if ask_firstname.lower() == accounts["First Name"].lower() and ask_secondname.lower() == accounts["Last Name"].lower():
                    print("Valid Account in system")
                    selected_account = accounts
                    found_both_names = True
            
            if found_both_names == True:
# Only allowed 3 attempts
                retry = 0
                
                password_found = False
                while True:
                    retry += 1
                    print("You only have 3 tries.")
                    print(f"You are on your {retry}/3 try")
                    if retry > 3:
                        return
                    password = input(f"Enter password for {ask_firstname} {ask_secondname}: ")
                    
                    if password == selected_account["Password"]:
                        password_found = True
                        break
                if password_found == True:
########################################## START OF DEPOSIT/WITHDRAW ##############################################################
                    print("=" * 30)
                    print("           Account Menu")
                    print("=" * 30)
                    print("1) Withdraw")
                    print("2) Deposit")
                    print(f"Account Balance: {selected_account["Account Balance"]}")
                    negative_balance = False
                    while True:
                        account_menu_choice = int(input("Enter from choice 1-2: "))
                        if account_menu_choice == 1:
                            withdraw_amount = float_errorhandling("how much will you like to withdraw? ")
                            if withdraw_amount > float(selected_account["Account Balance"]):
                                negative_balance = True
                            else:
                                negative_balance - False
                        if negative_balance == True:
                            debt_choice = input("Are you sure you want to be in debt? (y/n) ")
                            if debt_choice.lower() == "y":
                                new_withdraw_balance = float(selected_account["Account Balance"]) - withdraw_amount
                                selected_account["Account Balance"] = new_withdraw_balance
                                transaction_withdraw = f"{selected_account["First Name"]} withdrawed £{withdraw_amount} | New balance:{new_withdraw_balance}"
                                selected_account["Transaction"] = transaction_withdraw
                                with open ("bankinginformation.csv","w",newline="") as f:
                                    fieldnames = ["First Name","Last Name","Username","Email","Password","Account Balance","Transaction"]
                                    writecsv = csv.DictWriter(f,fieldnames=fieldnames)
                                    writecsv.writeheader()
                                    writecsv.writerows(self.account_list)
                                    print(f"You have got a new balance of {new_withdraw_balance}")
                                    return
                            if debt_choice == False:
                                break
                        elif account_menu_choice == 2:
                            deposit_amount = float_errorhandling("how much will you like to deposit? ")
                            new_deposit_balance = deposit_amount + float(selected_account["Account Balance"])
                            transaction_deposit = f"{selected_account["First Name"]} deposited £{deposit_amount} | New balance:{new_deposit_balance}"
                            selected_account["Transaction"] = transaction_deposit
                            with open ("bankinginformation.csv","w",newline="") as f:
                                    fieldnames = ["First Name","Last Name","Username","Email","Password","Account Balance","Transaction"]
                                    writecsv = csv.DictWriter(f,fieldnames=fieldnames)
                                    writecsv.writeheader()
                                    writecsv.writerows(self.account_list)
                                    print(f"You have got a new balance of {new_deposit_balance}")
                                    return
                    
                    with open ("bankinginformation.csv","w",newline="") as f:
                        fieldnames = ["First Name","Last Name","Username","Email","Password","Account Balance","Transaction"]
                        writecsv = csv.DictWriter(f,fieldnames=fieldnames)
                        writecsv.writeheader()
                        writecsv.writerows(self.account_list)
                        return
                if password_found == False:
                    continue
                        
            if found_both_names == False:
                print("Account first and last name doen't match.")
                retry = input("Try again? (y/n): ")
                if retry.lower() == "y":
                    bankingsystem.remove_account()
                    break
                elif retry.lower() == "n":
                    return
    def view_last_transaction(self):
        if len(self.account_list) == 0:
            print("No Accounts In Database.")
            return
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
            found_first = False
            for accounts in self.account_list:
                if ask_firstname.lower() == accounts["First Name"].lower():
                    found_first = True
                    break
            if found_first == False:
                print(f"Invalid user name {ask_firstname}")
                retry = input("Try again? (y/n): ")
                if retry.lower() == "y":
                    bankingsystem.remove_account()
                    break
                elif retry.lower() == "n":
                    return
# Checks for last name in database.
            ask_secondname = input("Last name of account: ")
            found_last = False
            for accounts in self.account_list:
                if ask_secondname.lower() == accounts["Last Name"].lower():
                    found_last = True
                    break
            if found_last == False:
                print(f"Invalid last name {ask_secondname}")
                retry = input("Try again? (y/n): ")
                if retry.lower() == "y":
                    bankingsystem.remove_account()
                    break
                elif retry.lower() == "n":
                    return
# Checks if both names match
            found_both_names = False
            for accounts in self.account_list:
                if ask_firstname.lower() == accounts["First Name"].lower() and ask_secondname.lower() == accounts["Last Name"].lower():
                    print("Valid Account in system")
                    selected_account = accounts
                    found_both_names = True
            
            if found_both_names == True:
# Only allowed 3 attempts
                retry = 0
                
                password_found = False
                while True:
                    retry += 1
                    print("You only have 3 tries.")
                    print(f"You are on your {retry}/3 try")
                    if retry > 3:
                        return
                    password = input(f"Enter password for {ask_firstname} {ask_secondname}: ")
                    
                    if password == selected_account["Password"]:
                        password_found = True
                        break
                if password_found == True:
########################################## START OF VIEW TRANSACTION ##############################################################
                    print(f"Last transaction was: {selected_account["Transaction"]}")
                    return
                if password_found == False:
                    continue
                        
            if found_both_names == False:
                print("Account first and last name doen't match.")
                retry = input("Try again? (y/n): ")
                if retry.lower() == "y":
                    bankingsystem.remove_account()
                    break
                elif retry.lower() == "n":
                    return    


class BankInformation():
    def __init__(self,firstname,lastname,email,password,balance):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.balance = balance
        self.transcation = []

bankingsystem = BankingSystem()