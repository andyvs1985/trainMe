
class Car:

	maxspeed = 0
	name = ""

	def __init__(self):
		self.__setMaxSpeed(100)
		self.maxspeed = 300
		self.name = "Super Car"

	def drive(self):
		print 'drive. maxspeed' + str(self.maxspeed)

	def __setMaxSpeed(self, speed):
		self.maxspeed = speed
		print ("hello")

redcar = Car()
redcar.drive()
# redcar.__maxspeed = 10
# redcar.setMaxSpeed(320)
