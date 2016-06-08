import random

class Die():
	"""docstring for Die class"""

	def __init__(self):
		""""""
		self.side = 0

	def throw(self):
		""" This method is for throw dice"""
		self.side=random.randint(1,6)

	def get_value(self):
		""" This method is for getting value for dice thrown"""
		return self.side

# is an Instance of class Die
my_object = Die()
for i in range(1,10):
	my_object.throw()
	#Innvoking the method throw()
	my_object.throw()
	die_value = my_object.get_value()
	print "The value thrown is",die_value
