# this demonstration is to show how python objects are constructed and assigned

class DemoClass:
	""" docstring of DemoClass"""
	pass


# lets create an intance of a class DemoClass
my_instance_1 = DemoClass() # This is nothing but constructor.
print(id(my_instance_1))
print(type(my_instance_1))


# lets assign the instance to another label
my_instance_2 = my_instance_1 # This is nothing but a assigning the object
print(id(my_instance_2))
print(type(my_instance_2))
