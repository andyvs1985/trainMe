a = []

list = [12,3,4,'anand',12,'raj']
# user_input = raw_input("Please Enter a value : ")

for i in list:
	if len(a)>=1:
		if type(a[0]) == type(i):
			a.append(i)
			print "Value appended to List is : ", i
		else:
			print "This value is not typecast : ", i
	else:
		a.append(i)
		print "Initial Value appended to List is : ", i

