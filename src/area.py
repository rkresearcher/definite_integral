from equation import *
def area(lst):
	l_lst = len(lst)
	area_of_curve = 0
	for i in range(len(lst)-1):
		if lst[i] == lst[i+1]:
			print ('square')
			area  = 1*(lst[i+1])
		else:
			area_t  = 0.5*(lst[i+1]-lst[i])
			area_s = 1*lst[i]
			area  = area_t + area_s
		area_of_curve += area
	return area_of_curve


p = []

for i in range(10):
	p.append(i)	
# data creation for linear equation
y = equation ('lin', 2,3)
#for j in range(1,100):
in_data = []
area_data = []
for i in frange(0,3,1):
#	print(i)
	y1 = y(i)
#	print (y1)
	in_data.append(y1)

area_for_data = area(in_data)
