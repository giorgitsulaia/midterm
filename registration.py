import database 

def register_customer():
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        account_number = input("Enter your account number: ")

        if database.validate_account_number(account_number):
            if account_number not in database.customers:
                database.customers[account_number] = {
                    'first_name': first_name,
                    'last_name': last_name
                }      
                database.balances[account_number]=0
                print("you have registered successfully.")
            else:
                print("Account number already exists.")
        else:
            print("Invalid account number format.")
        
    
if __name__ == "__main__":
    while True:
        register_customer()
        choice = input("Do you want to register new account? (Y or N): ")
        if choice.upper() == 'Y':
            continue
        elif choice.upper() == 'N':
            break
        else:
            print("Invalid input")
