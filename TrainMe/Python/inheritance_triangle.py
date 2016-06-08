# this is the program to find the area of triangle.

class Trianlge:
	""" Base class of Trianlge"""

	def __init__(self, base, height):
		self.base = base
		self.height = height

	def areaOfTriangle(self):
		area = self.base * self.height /2
		print area

instance_1 = Trianlge(2,4)
instance_1.areaOfTriangle()
#reload(instance_1.areaOfTriangle) 
