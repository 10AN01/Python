from bankingfunctions import bankingsystem
def menu():
    print("=" * 50)
    print("                  BANKING SYSTEM                    ")
    print("=" * 50)
    print("1. Add Banking Account")
    print("2. Remove Banking Account")
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
menu()