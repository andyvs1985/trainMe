

def hello(func):
	"""
	"""
	print 'hello'
	return func()

@hello
def greeters():
	"""
	"""
	print 'ram'

@hello
def kk():
	"""
	"""
	print 'kk'

@hello
def raj():
	"""
	"""
	print 'raj'

@hello
def greeter():
	"""
	"""
	print 'pal'

# aa = hello(greeters)
# print aa