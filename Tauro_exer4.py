securityPin = None
message = "omsim"
def menu():
	print("0 - Exit Program")
	print("1 - Unlock Secret Message")
	print("2 - Change Security Pin")
	
def secret_message(securityPin):
	if securityPin = None:
		securityPin = manage_pin(securityPin)
		return securityPin
	else:
		check_pin = input("Enter your pin: ")
		if check_pin = securityPin:
			print(message)
		return securityPin
		else:
		print("Incorrect Pin. Pls try again")
		return securityPin


def manage_pin(securityPin):
	if securityPin is None:
		print("No security PIN!")
		while securityPin is None:
			new_pin = input("Please enter a new PIN (2 letters, 2 numbers): ")
			if not new_pin.isalnum() or not len(new_pin) == 4:
				print("Invalid PIN")
			else:
				securityPin = new_pin
				print("Security PIN Enabled!")
				return securityPin
	else:
		input_pin = input("Enter your PIN: ")
		if input_pin == securityPin:
			managing_pin = True
			while managing_pin: 
				new_pin = input("Please change you PIN (2 letters, 2 numbers): ")
				if not new_pin.isalnum() or not len(new_pin) == 4:
				print("Invalid PIN")
			else:
				securityPin = new_pin
				print("Security PIN Enabled!")
				return securityPin
		else:
			print

#main loop
menu()
choice = int(input("Choose from the options: "))
if (choice > 2):
	exited = False
	print("Invalid choice. Wag ka bida bida may option na eh")
elif (choice == 0):
	exited = False
	print("You have exited the program")
elif (choice == 1):
	if securityPin == none:
		print("You have no security pin")
		securityPin = input("Please enter security pin (2 Letters, 2 Numbers): ")
		if securityPin == "ab12":
			securityPin == True
		else:
			print("Invalid securityPin")
	else:
		check = input(securityPin)	
		secret_message(securityPin)
		
elif (choice == 2):
	manage_pin(securityPin)
	print("Managing security pin")
