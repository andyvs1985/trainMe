# x = [1, 2, 3, 3, 2, 5]
# for i in xrange(len(x)):
# 	for j in xrange(i+1, len(x)):
# 		 if x[i] == x[j]:
# 			print x[i]


x = [1, 2, 3, 3, 2, 5]
[i for i in x if x[i] == 1]