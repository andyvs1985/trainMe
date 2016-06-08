# # Program to validate the integer values

# def CheckInt(userinput):
# 	"""
# 	"""
# 	if type(userinput) == int:
# 		return userinput
# 	else:
# 		print "please enter only integer"
# 		return False


# # CheckInt(2)

def CheckInt(userinput):
    # isbn=raw_input('Please enter the 10 digit number: ')

    try:
        int(userinput)  # we try to get an int from the input... 

    except:
    	import pdb; pdb.set_trace()
        print "List will accept only integer "
        return False

    return userinput


