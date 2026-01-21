from bankingfunctions import BankingSystem
bankingsystem = BankingSystem()
def menu():
    print("=" * 50)
    print("                  BANKING SYSTEM                    ")
    print("=" * 50)
    print("1. Add Banking Account")
    print("2. View Bank Accounts")
    print("3. Remove Banking Account (Required Login)")
    print("4. Deposit (Required Login)")
    print("5. Withdraw (Required Login)")
    print("6. View Transaction History (Required Login)")
    print("7. End Program")
    print("=" * 50)
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            bankingsystem.add_account()
            break
        elif choice == 2:
            bankingsystem.view_account()
        elif choice == 3:
            bankingsystem.remove_account()
            break
        elif choice == 4:
            print("Working")
            break
        elif choice == 5:
            print("Working")
            break
        elif choice == 6:
            print("Working")
            break
        elif choice == 7:
            print("Bye!")
            break
menu()