from equation import *
from my_math import *
def fun_exp():
	ar = ['lin','qua','tri', 'for', 'fiv', 'six', 'sev',
			'eig', 'nin', 'ten', 'ele', 'twe', 'thir',
				'fourt','fift', 'sixt', 'sevet', 'eight', 'nint','twen', 'tweno',
					'twent', 'twenth', 'twenf', 'twenfi', 'twensi', 'twense', 'twenei']
	p = []
	for i in ar:
		print (i)
#		y = equation(i,1)
		
		p.append(y)
	return p

def d_fnn():
	ar = ['lin','qua','tri', 'for', 'fiv', 'six', 'sev',
			'eig', 'nin', 'ten', 'ele', 'twe', 'thir',
				'fourt','fift', 'sixt', 'sevet', 'eight', 'nint','twen', 'tweno',
					'twent', 'twenth', 'twenf', 'twenfi', 'twensi', 'twense']
	
	d_p = [1]
	for i in range(len(ar)):
		y = equation(ar[i],i+2)
		d_p.append(y)
	return d_p

def nn_out(x):
	n = d_fnn()
#	print (n[1](x))

	w = weight(1,len(n))
	n_x = w[0][0]
	for i in range(len(n)-1):
		print (i)
#		exit()
		#print (w[0][i])

		#print (n[i](x))
		n_x += w[0][i+1]*n[i+1](x)
	return n_x

'''def nn_dash():
	w = weight(1,len(n))
	n_x = w[0][0]
	for  i in range(len(n)-1)):
		n_x = n
'''
def f_error(y,low_l,up_l):
	error = 0.5	
	err_lst = []
	for i in frange(low_l,up_l,0.1):
		error1 = (y(i)-nn_out(i))**2
		error += error1
		err_lst.append(error1)
	return 0.5*error,err_lst

y = equation ('qua', 1)
a = 0
b = 2
y1,y2 = f_error(y,a,b)
print (y2)

def d_err():
	

def error_min(y,a,b):
	d_f = d_fnn()
	n = d_fnn()
	y,e = f_error(y,a,b)
	for i in range(len(n)):
		for i in range(len(n)):
			w[0][i] -= w[0][i] +lr*e[i]*
