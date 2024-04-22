import database

def add_balance():
    account_number = input("Enter your account number for transaction money: ")
    if not database.validate_account_number(account_number):
        print("Invalid account number format.")
        return
    if account_number in database.customers:
        amount = input("Enter the amount of money you want to deposit: ")
        if amount.isdigit():
            amount = float(amount)
            database.balances[account_number] += amount
            print(f"Balance filled with {amount} GEL.")
        else:
            print("Invalid amount entered.")
    else:
        print("Account number does not exist.")
    

def transfer_money():
    main_account = input("Enter your account number: ")
    if not database.validate_account_number(main_account):
        print("Invalid account number format.")
        return
    
    if main_account in database.customers:
        recipient_account = input("Enter the account number you want to transfer money to: ")
        if not database.validate_account_number(recipient_account) or recipient_account not in database.customers:
            print("The account number does not exist.")
            return
        amount = input("Enter the amount of money you want to transfer: ")
        if amount.isdigit():
            amount =  float(amount)
            if database.balances[main_account] >= amount:
                database.balances[main_account] -= amount
                database.balances[recipient_account] +=amount
                print(f"You have successfuly transferred {amount} GEL to {database.customers[recipient_account]['first_name']} {database.customers[recipient_account]['first_name']}.")
            else:
                print("Not enough money.")
        else:
            print("Invalid money entered.")
    else:
        print("Entered (main) account number does not exist.")

if __name__ == "__main__":
        while True:
            print("Enter 1 to add Balance: ")
            print("Enter 2 to Transfer money: ")
            choice = input("Choose an operation (1 or 2): ")
            
            if choice == '1':
                add_balance()
            elif choice == '2':
                transfer_money()
            else:
                print("Invalid choice")