from getpass import getpass
def str_errorhandling(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input.isalpha():
            return user_input
        else:
            print("Invalid. Letters ONLY")
            
def email_errorhandling(prompt):
    while True:
        user_input = input(prompt)
        if "@" in user_input:
            part = user_input.split("@")
            if len(part) !=  2:
                print("Invalid format")
            else:
                if part[0] == "" or part[1] == "":
                    print("Invalid Format.")
                else:
                    return user_input
        else:
            print("Invalid Email.")

def password_length(prompt):
    while True:
        userpassword = getpass(prompt)
        if len(userpassword.strip()) > 5:
            return userpassword
        else:
            print("Password is not long enough")

def password_secure(userpassword):
    special_characters = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_",
    "=", "+", "{", "}", "[", "]", "|", "\\", ":", ";", "\"", "'",
    "<", ">", ",", ".", "?", "/"
    ]
    hasupper = False
    haslower = False
    hasdigit = False
    hasspecial = False
    
    for a in userpassword:
        if a.isupper():
            hasupper = True
        if a.islower():
            haslower = True
        if a.isdigit():
            hasdigit = True
        if a in special_characters():
            hasspecial = True
    
