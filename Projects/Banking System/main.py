from bankingfunctions import BankingSystem
bankingsystem = BankingSystem()

def menu():
    while True:
        print("=" * 50)
        print("                  BANKING SYSTEM                    ")
        print("=" * 50)
        print("1. Add Banking Account")
        print("2. View Bank Accounts")
        print("3. Remove Banking Account (Required Login)")
        print("4. Deposit/Withdraw (Required Login)")
        print("5. View Last Transaction (Required Login)")
        print("7. End Program")
        print("=" * 50)
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                bankingsystem.add_account()
            elif choice == 2:
                bankingsystem.view_account()
            elif choice == 3:
                bankingsystem.remove_account()
            elif choice == 4:
                bankingsystem.deposit_withdraw_account()
            elif choice == 5:
                bankingsystem.view_last_transaction()
            elif choice == 7:
                print("Bye!")
                break
            else:
                print("Invalid Option")
        except ValueError:
            print("Invalid")
menu()