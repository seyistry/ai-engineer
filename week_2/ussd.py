# create a commandline interface for USSD

print("Welcome to the USSD service")

balance = 100

def main_menu(balance):
    print("Main Menu:")
    print("1. Check Balance")
    print("2. Buy Airtime")
    print("3. Transfer")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        check_balance()
    elif choice == "2":
        buy_airtime()
    elif choice == "3":
        transfer(balance)
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu(balance)

def check_balance():
    print(f"Your current balance is N{balance}.")
    main_menu(balance)

def buy_airtime():
    amount = input("Enter amount to buy airtime: ")
    print(f"You have purchased ${amount} airtime.")
    main_menu(balance)

def transfer(balance):
	recipient = input("Enter recipient's number: ")
	amount = input("Enter amount to transfer: ")
     
	# Check if balance is sufficient
	if float(amount) > balance:
		print("Insufficient balance for this transfer.")
		main_menu(balance)
	balance -= float(amount)
	print(f"You have transferred N{amount} to {recipient}.")
	main_menu(balance)

main_menu(balance)