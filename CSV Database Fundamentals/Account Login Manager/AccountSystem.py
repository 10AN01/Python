import csv


class AccountSystem():
#Sets a list and checks if file exist.
    def __init__(self):
        self.account_list = [
            
        ]
        try:
            with open ("useraccounts_database.csv","r") as f:
                readcsv = csv.DictReader(f)
                self.account_list.extend(readcsv)
        except FileNotFoundError:
            self.account_list = []
    def add_account(self):
        print("You have chosen to register an account.")
#Allows user to import data.
        username =  input("Enter a username you'll like to register with: ")
        while True:
            email = input("Enter your email address: ")
            email_split = email.split("@")
            if len(email_split) != 2:
                print("Invalid Email.")
            elif email_split[0] == "" or email_split[1] =="":
                print("Invalid Email")
            else:
                print("Valid Email")
                break
        while True:
            password = input("Enter a password: ")
            password_confirm = input("Enter password again: ")
            if password_confirm == password:
                print("Password matches!")
                break
            else:
                print("Password doesn't match. Try Again")
            
            
        datainputted =  account_information(username,email,password)
# Turns into raw data
        data_dict = {
            "Username":datainputted.username,
            "Email":datainputted.email,
            "Password":datainputted.password
        }
        self.account_list.append(data_dict)
# Put's file in write mode. Gives header and puts in data.
        with open ("useraccounts_database.csv","w", newline="") as f:
            fieldnames = ["Username","Email","Password"]
            writecsv = csv.DictWriter(f, fieldnames=fieldnames)
            writecsv.writeheader()
            writecsv.writerows(self.account_list)
            
            
    def view_account(self):
        counter = 0
        for accounts in self.account_list:
            counter += 1
            print(f"- - - - - - Account {counter} - - - - - -")
            print(f"Username: {accounts['Username']}")
            print(f"Email: {accounts['Email']}")
            print(f"Password: {accounts['Password']}")
            
    def remove_account(self):
        print("You have chosen to remove an account")
        counter = 0
        for accounts in self.account_list:
            counter += 1
            print(f"- - - - - - Account {counter} - - - - - -")
            print(f"Username: {accounts['Username']}")
            print(f"Email: {accounts['Email']}")
            print(f"Password: {accounts['Password']}")
        while True:
            remove_account = input("Enter an account username that you'll like to remove: ")
            if remove_account == accounts['Username']:
                self.account_list.remove[remove_account]
                print(f"Deleted: {remove_account}")
                break
            elif remove_account != accounts['Username']:
                print(f"Invalid usernamed called: {remove_account}")
        



class account_information():
    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password
