# Python program to accepts only integers.
from checkInt import CheckInt

class IntList:
	"""
	Integer List class
	"""

	def __init__(self,myList,userInput):
		"""
		Special class
		"""
		self.mylist = myList
		self.rawinput = userInput

	def AppendInt(self):
		"""
		"""
		lists = self.mylist
		lists.append(self.rawinput)

	def ExtendInt(self):
		"""
		"""
		lists = self.mylist
		lists.extend(str(self.rawinput))

	def InsertInt(self):
		"""
		"""
		lists = self.mylist
		lists.insert(0, self.rawinput)

	def PopInt(self):
		"""
		"""
		lists = self.mylist
		lists.pop()

	def RemoveFromList(self):
		"""
		"""
		lists = self.myList
		lists.remove()

userInput = raw_input("Please Enter a number : ")
# aa = CheckInt(userInput)
myList = []
print "This is the empty list", myList

try:
	int(userInput)
	list_update = IntList(myList, userInput)

	list_update.AppendInt()
	print "Adding to list : ", list_update.mylist

	list_update.ExtendInt()
	print "Extending the list iterables",list_update.mylist

	list_update.InsertInt()
	print "Inserting value at the index", list_update.mylist

	list_update.PopInt()
	print "Popping the value from the end", list_update.mylist
except (ValueError,StopIteration):
	print "List accepts only Integer"
	# return False

else: 
	print "successfully list is manipulated."

# return True