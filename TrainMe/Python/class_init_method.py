# Python __init__ method also called as Python Special methods

class CurrnetAccout:
	"""docstring for CurrnetAccout"""
	def __init__(self, customer_name):
		"""The __init__() method is called after the instance is created"""
		self.name = customer_name
		self.balance = 10000

	def get_customer_name(self):
		"""This method returns the name of the customer"""
		return	self.name

	def get_customer_balance(self):
		"""This method returns the age of the customer"""
		return self.balance

account_holder = CurrnetAccout("Rita j")
if(account_holder):
	print "The customer name is", account_holder.get_customer_name()
	print "The customer balance is Rs.",account_holder.get_customer_balance()