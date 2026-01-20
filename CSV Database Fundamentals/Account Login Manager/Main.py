from AccountSystem import AccountSystem
accountsystem = AccountSystem()
print(" = = = = = = Account Menu = = = = = =")
print("1) Add Account")
print("2) Remove Account")
print("3) View Accounts")
print("4) End Program")
while True:
    choice = int(input("Enter a choice: "))
    if choice == 1:
        accountsystem.add_account()
        break
    elif choice == 2:
        accountsystem.remove_account()
        break
    elif choice == 3:
        accountsystem.view_account()
        break
    elif choice == 4:
        print("Bye!")
        break