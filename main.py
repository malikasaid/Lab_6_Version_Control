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

# Malika Saidmuradova
def decode(code):
	# Convert string to list of characters
    code_list = list(code)
    password =""
    for i in range(len(code_list)):
        if code_list[i] == "0":
            password += "7"
        elif code_list[i] == "1":
            password += "8"
        elif code_list[i] == "2":
            password += "9"
        elif code_list[i] == "4":
            password += "1"
        elif code_list[i] == "5":
            password += "2"
        elif code_list[i] == "6":
            password += "3"
        elif int(code_list[i]) >= 7 and int(code_list[i]) <= 9:
            password += str(int(code_list[i]) - 3)
        else:
            password += str(int(code_list[i]) + 3)
    return password
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
			password = input("Please enter your password to decode: ")
			decoded_password = decode(password)
			print("Your password has been decoded: " + decoded_password)
			print()

		elif user_selection == 3:
			break
		else:
			print("Invalid input. Please try again.")
			print()
