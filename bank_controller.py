from bank_model import Bank_Account
#from bank_view import Bank_Interface

#my_interface = Bank_Interface()
my_database = Bank_Account()




print("Please enter your username")
username = input()
print("please enter your name")
fullname = input()
print("Pleae enter a password")
password = input()
credentials = [username, fullname, password]
		

print(username, fullname, password)


my_database.insert_user_info(username, fullname, password)
print(my_database.select_table_user())