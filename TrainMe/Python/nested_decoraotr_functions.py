def outside(x=0):
	def printHam():
		print x
	return printHam

myFunc = outside(5)
myFunc()
