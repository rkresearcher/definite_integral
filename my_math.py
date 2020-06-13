import random
def fact(n):
	if n==1:
		return 1
	return n*fact(n-1)
print (fact(12))
def weight(n,m):
	p = []
	for row in range(n):
		q = []
		for col in range(m):
			q.append(random.random())
		p.append(q)
	return p
def mat_mul(x,y):
		result = weight(len(x),len(y[0]))
		print (len(x))
		if len(x)==len(y[0]):
			for row in range(len(x)):
 #                               print (i)
				for col in range(len(y[0])):
					for col_y in range(len(y)):
						result[row][col] += x[row][col_y]*y[col_y][col]
			return result
		else:
			print("dimension not match")
#                return result
#print(weight(2,2,4)*weight(2,2,3))
#p = weight(1,5)
#q = weight (5,1)
#print(p)
#print (q)
#t = mat_mul(p,q)
#print (t)

