# Joe Kan   3/6/2023   Partner: Malika Saidmuradova   Group: 40

def print_menu():
	# Print the menu
	print("Menu")
	print("-------------")
	print("1. Encode")
	print("2. Decode")
	print("3. Quit")
	print()

def encode(code):
	# Takes in a string of numbers and changes them by adding 3 to each
	code_list = list(code)
	code_string = ""
	for i in range(len(code_list)):
		if code_list[i] == "7":
			code_string += "0"
		elif code_list[i] == "8":
			code_string += "1"
		elif code_list[i] == "9":
			code_string += "2"
		else:
			code_string += str(int(code_list[i]) + 3)
	return code_string

if __name__ == "__main__":
	while True:
		# Print the menu
		print_menu()

		# Get user selection
		user_selection = int(input("Please enter an option: "))
		if user_selection == 1:
			# Encode password
			password = input("Please enter your password to encode: ")
			encoded_password = encode(password)
			print("Your password has been encoded and stored!")
			print()
		elif user_selection == 2:
			# Decode password
			# Partner's code goes here
			print()
		elif user_selection == 3:
			break
		else:
			print("Invalid input. Please try again.")
			print()
