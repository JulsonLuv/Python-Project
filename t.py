def deposit():
    while True:
        amount = input("Wha would you like to Desposit? $")
        if amount.isdigit():
            amount =int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("Please enter a Number.")
    
    return amount
deposit()