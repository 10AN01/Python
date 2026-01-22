def int_errorhandling(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid Number")
            
def float_errorhandling(prompt):
    while True:
        try:
            floaterror = float(input(prompt))
            return round(floaterror,2)
        except ValueError:
            print("Invalid Number")
            
def str_errorhandling(prompt):
    while True:
        try:
            return str(input(prompt))
        except ValueError:
            print("Invalid Name")
            
def email_errorhandling(prompt):
    while True:
        email = input(prompt)
        email_split = email.split("@")
        if len(email_split) != 2:
            print("Invalid Email")
        elif email_split[0] == "" or email_split[1] == "":
            print("Invalid Email")
        else:
            return email
        