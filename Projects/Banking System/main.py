from bankingfunctions import BankingSystem
bankingsystem = BankingSystem()
def menu():
    print("=" * 50)
    print("                  BANKING SYSTEM                    ")
    print("=" * 50)
    print("1. Add Banking Account")
    print("2. Remove Banking Account (Required Login)")
    print("3. Deposit (Required Login)")
    print("4. Withdraw (Required Login)")
    print("5. View Transaction History (Required Login)")
    print("6. End Program")
    print("=" * 50)
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            bankingsystem.add_account()
            break
        elif choice == 2:
            bankingsystem.remove_account()
            break
        elif choice == 3:
            print("Working")
            break
        elif choice == 4:
            print("Working")
            break
        elif choice == 5:
            print("Working")
            break
        elif choice == 6:
            print("Bye!")
            break
def tryagain_remove():
    while True:
        answer_restart = input("Would you like to try again? (Yes/No) ")
        if answer_restart.lower() == "Yes":
            bankingsystem.remove_account()
        elif answer_restart.lower() == "No":
            menu()
        else:
            print("Invalid Option. Try Again")
menu()