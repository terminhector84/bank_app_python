import sqlite3

class Bank_Account:

	def __init__(self):
		self.conn = sqlite3.connect("bank_account.db")
		self.cursor = self.conn.cursor()

	def create_user_table(self):
		self.cursor.execute(''' CREATE table if not exists user_account(
								user_id varchar(25) primary key,
								fullname varchar(25),
								pwd varchar(25)
								)''')
		self.conn.commit()

	def create_checking_table(self):
		self.cursor.execute(''' CREATE table if not exists checking_account(
								checking_id int primary key,
								balance real(10) default 150,
								deposit_amt real(10),
								user_id varchar,
								foreign key(user_id) references user_account(user_id)
								) ''')
		self.conn.commit()

	def create_savings_table(self):
		self.cursor.execute(''' CREATE table if not exists savings_account(
								savings_id int primary key,
								balance real(10) default 0,
								deposit_amt real(10),
								user_id varchar,
								foreign key(user_id) references user_account(user_id)
								) ''')
		self.conn.commit()

	def closeConnection(self):
		self.conn.close()

#this function allows the app to create a user account and insert this value into the database
	def insert_user_info(self, user_id, fullname, pwd):
		self.cursor.execute('INSERT INTO user_account(user_id,fullname,pwd) values (?,?,?)', (user_id, fullname, pwd))
		self.conn.commit()


#connect user account to checking acccount
	def conn_user_to_checking(self):
		self.cursor.execute('select * from user_account join checking_account on user_account.user_id == checking_account.user_id')
		self.conn.commit()

#connect user account to checking account
	def conn_user_to_savings(self):
		self.cursor.execute('select * from user_account join checking_account on user_account.user_id == checking_account.user_id')

#connect user account to both accounts
	def conn_user_to_both_accounts(self):
		self.cursor.execute('select * from user_account join checking_account on user_account.user_id == checking_account.user_id join savings_account on user_account.user_id == savings_account.user_id')


#this function allows the user to deposit dinero into the checking account
	def desposit_amt_checking(self, amt):
		self.cursor.execute('insert into checking_account(deposit_amt) values (?)', (amt))
		self.conn.commit()

#this function allows the user to deposit dinero into the savings account
	def desposit_amt_savings(self, amt):
		self.cursor.execute('insert into savings_account(deposit_amt) values (?)', (amt))
		self.conn.commit()

#this function displays the user information
	def select_table_user(self):
		self.cursor.execute("SELECT * FROM user_account")
		return self.cursor.fetchall()[0][0]

#this function shows the balance in the checking account
	def display_checking_balance(self):
		self.cursor.execute("SELECT balance FROM checking_account join user_account on checking_account.user_id == user_account.user_id")
		return self.cursor.fetchall()[0][0]

#this function shows the balance in the savings account
	def display_savings_balance(self):
		self.cursor.execute("SELECT balance FROM savings_account join user_account on savings_account.user_id == user_account.user_id")
		return self.cursor.fetchall()[0][0]

#deposit amount from checking account
	def deposit_checking(self, amt, Acc_id):
		self.cursor.execute("update checking_account set balance =? where checking_id=?", ((balance + amt), Acc_id))
		self.conn.commit()

#deposit amount from savings account
	def deposit_savings(self, amt, Acc_id):
		self.cursor.execute("update savings_account set balance =? where savings_id", ((balance + amt), Acc_id))	
		self.conn.commit()

#withdraw amount from checking account
	def withdraw_checking(self, amt, Acc_id):
		self.cursor.execute("update checking_account set balance =? where checking_id=?", ((balance - amt), Acc_id))
		self.conn.commit()

#withdraw amount from savings account
	def withdraw_savings(self, amt, Acc_id):
		self.cursor.execute("update savings_account set balance =? where savings_id=?", ((balance - amt), Acc_id))	
		self.conn.commit()


#transfer amount from checking to savings
	def transfer_to_savings(self, amt, Acc_id):
		self.cursor.execute("update checking_account set balance =? where checking_id=?", ((balance - amt), Acc_id))	
		self.cursor.execute("update savings_account set balance =? where savings_id=?", ((balance + amt), Acc_id))
		self.conn.commit()


#transfer amount from savings to checking
	def transfer_to_checking(self, amt, Acc_id):
		self.cursor.execute("update savings_account set balance =? where savings_id=?", ((balance - amt), Acc_id))
		self.cursor.execute("update checking_account set balance =? where checking_id=?", ((balance + amt), Acc_id))	
		self.conn.commit()

#ask user for credentials to create account
	def insert_checking(self, username, pwd):
		self.cursor.execute('insert into user_count(user_id, user_pwd) values (?,?)', (username, pwd))
		self.conn.commit()
 
	

if __name__== "__main__":
	my_database = Bank_Account()
	my_database.create_user_table()
	my_database.create_checking_table()
	my_database.create_savings_table()
	my_database.closeConnection() 