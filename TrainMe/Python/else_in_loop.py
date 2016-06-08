def func(array):
	# import pdb; pdb.set_trace()
	for i in array:
		if i%2==0:
			print(i)
			break
	else:
		print("nothing")

print "1st Case"
a = [2]
func(a)

print"2nd case"
a = [1]
func(a)