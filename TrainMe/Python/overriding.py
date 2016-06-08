# Overriding

class BankAccount():
	def __init__(self, account_name = "current account", balance = 20000):
		self.account_name = account_name
		self.balance = balance

acc_obj = BankAccount()
print(acc_obj.account_name)
print(acc_obj.balance)

print ("Overriding the balance")
acc_obj.balance = 1000
print(acc_obj.balance)
