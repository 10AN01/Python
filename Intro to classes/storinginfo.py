# Able to add information (e.g. email,password,username,social)
accountdata = []

def menu():
    print("- - - - | Account Manager| - - - -")
    print("- - - - 1.Add Information - - - -")
    print("- - - - 2.Remove Information - - - -")
    print("3.View Information(Requires passwords)")
    print("- - - - - 4.End Program - - - - -")
    while True:
        choice = int(input("Enter a choice 1-4: "))
        if choice == 1:
            add_info()
        if choice == 2:
            
        if choice == 3:
            
        if choice == 4:
            
        else:
            print("Invalid Choice. Try Again")   

class Account:
    def __init__(self,user_username,user_email,user_password,user_social):
        self.username = user_username
        self.email = user_email
        self.password = user_password
        self.social = user_social

account_data_dict = {
    user_username
}

def add_info():
    print("You have chosen to store information.")
    username = input("Enter username: ")
    print("What does your email end with?")
    print("1. @gmail.com")
    print("2. @yahoo.com")
    print("3. @outlook.com")
    print("4. @hotmail.com")
    print("5. @icloud.com")
    print("6. @mail.com")
    while True:
        email_extension = int(input("Enter a email extension 1-6: "))
        if email_extension >= 1 and email_extension <= 6:
            print("")
            break
        else:
            print("Please pick an option from 1-6.")
        if email_extension == 1:
            extension = "@gmail.com"
        elif email_extension == 2:
            extension = "@yahoo.com"
        elif email_extension == 3:
            extension = "@outlook.com"
        elif email_extension == 4:
            extension = "@hotmail.com"
        elif email_extension == 5:
            extension = "@icloud.com"
        elif email_extension == 6:
            extension = "@mail.com"
        else:
            print("Invalid")
    email = input("Enter email before the @: ")
    print("email is ")