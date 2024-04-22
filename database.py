customers = {}
balances = {}

def validate_account_number(account_number):
    return (len(account_number)==5 and account_number.startswith('TB') and account_number[2:].isdigit())

