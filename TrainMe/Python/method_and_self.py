class DemoClass:
	"""docstring of DemoClass"""

	# Here we are trying to run this fils without self.
	# this is to know why the self is really required.
	# if not using self in the demo_class method, it throws the below TypeError.
	# TypeError: demo_class() takes no arguments (1 given)
	def demo_class(self):
		"""docstring of demo_call method"""
		print ("I am demonstration method.")
		print(id(self))

my_object = DemoClass()
print(id(my_object))
my_object.demo_class()
import pdb; pdb.set_trace()
my_object_2 = my_object
