import random
def generatepassword():
    s = ""
    for i in range(10):
        s = s + chr(random.randint(50, 100))
    return s
    

print("|\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|")
print("|*******************MENU******************|")
print("|***********(1)Random password************|")
print("|**(2)Random password + with preference***|")
print("|*****************(3)Exit*****************|")
print("|\/\/\/\/\/\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/|")

while True:
    options = int(input("What would you like to do?  "))
    if options == 1:
        print("This is your random password:",generatepassword())
    elif options == 2:
        Userschoice = input("Enter in what you would like in your password: ")
        print("This is your random password including with your characters:",Userschoice,generatepassword())
    elif options == 3:
        print("You have now exited the program!")
        break