# Program to check the factorial of the argument "numer"

# def factorial(numb):
# 	prod = 1
# 	for i in range(numb):
# 		prod = prod * (i+1)
# 		print prod
# 	return prod

# print (factorial(5))


# def fact(number):
# 	if number <= 1:
# 		return 1 
# 	else:
# 		print number
# 		return number * fact(number - 1)

# print (fact(5))

# Recursive program on string
# explode ('hello') --> 'h e l l o'
def explode(word):
	if len(word) <= 1:
		return word
	else:
		return word[0] + ' ' + explode(word[1:])

print (explode('hello'))