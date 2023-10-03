#This program will unlock a secret message using a security PIN 
#Created by Yanika Illi J. Tauro - B1L Oct 3, 2023 with the help of Euan Tabamo


securityPin = None
message = "Heto na ang napakasecret na message: grabe ka na bestie"

def menu():
	print("0 - Exit Program")
	print("1 - Unlock Secret Message")
	print("2 - Change Security Pin")

	num = int(input("Choose from the items above: "))
	return num
	

def secret_message(securityPin):
	if securityPin is None:
		securityPin = manage_pin(securityPin)
		return securityPin
	else:
		check_pin = input("Enter your pin: ")
		if check_pin == securityPin:
			print(message)
			return securityPin
		else:
			print("Incorrect Pin. Please try again")
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
			print("Wrong PIN!")
			return securityPin

#Main loop program
RUNNING = True
while RUNNING:
	choice = menu()
	if choice == 0:
		RUNNING = False
		print("You have exited the program")
	elif choice == 1:
		securityPin = secret_message(securityPin)
	elif choice == 2:
		securityPin = manage_pin(securityPin)
	else:
		print("Invalid choice: Wala sa options yung choice mo bhie")