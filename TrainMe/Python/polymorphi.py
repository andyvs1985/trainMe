class Room:
	def __init__(self, door):
		self.door = door

	def open(self):
		self.door = open()

	def closed(self):
		self.door = closed()

	def is_open(self):
		self.door = is_open()

dr = Room('ss')
dr.open()
dr.closed()
dr.is_open()