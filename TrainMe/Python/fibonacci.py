# Python program to display the Fibonacci sequence up to n-th term using recursive functions
# Sequence format
def fibonacci1(n):
	"""
	param n : is the length of the fibonacci sequence
	"""
	# Setting the base case here with n=1 and n=2
	if n == 1 or n ==2:
		return 1
	return fibonacci1(n-1) + fibonacci1(n-2)

# Loop fibonnaci
def fibonnaci2(n):
	fa,la = 1,1
	for i in range(n-1):	
		fa,la = la, fa+la
	return fa

# Generator : is vender machine, does not produce all the result soon but ask and get
def fibonnaci3():
	fa,la=1,1
	while True:
		yield fa
		fa, la=la, fa+la

n = 0
for i in fibonnaci3():
	if n>=10:
		break;
	print i
	n +=1

# for i in range():
# 	print (fibonnaci3(i))