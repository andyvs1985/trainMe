# Public, Protected and Private Variables in python

# Public
# By default all member variables are public.

# Example

class Cup:
	"""Dockstring of cup class"""
	def __init__(self):
		self.color = None
		self._brand= None # Protected Variable
		self.__content = None # Private Variable
		print self._brand,self.__content, self.color


	# def fill(self,beverage):
	# 	self._content = beverage
	# 	print self._content

	# def empty(self):
	# 	self._content = None

# Instance of Cup class
redCup = Cup()
redCup._content = "tea"
redCup._Cup__brand = "rad"
# redCup.color = "red"
# redCup.content = "tea"

# redCup.empty()
# redCup.fill._content

