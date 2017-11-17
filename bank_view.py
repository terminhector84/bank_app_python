class Bank_Interface:

	def showOutput(self, output):
		print(output)

	def takeInput(self, prompt):
		return input(prompt)

	#def ask_for_credentials(self, answer):
	
	#	print("I am a new customer type 1")
	#	return input(answer)



	def log_in(self, username, password):
		print("Please enter your username")
		username = input()
		print("Please enter your password")
		password = input()


	def choose_option(self):
		print("1. I want to check my balance")
		print("2. I want to withdraw money")
		print("3. I want to deposit money")
		print("4. I want to transfer dinero to another account ")



		
