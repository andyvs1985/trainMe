def create_counter(i):
	print('create_counter()')
	# import pdb; pdb.set_trace()
	while True:
		yield i
		print('increment n')
		i += 1

instance_c = create_counter(2)
next(instance_c)