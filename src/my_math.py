from equation import *
import random


def mean(lst):
	p = 0.0
	for i in lst:
		p += i
		return p/len(lst)
def max_relu(x):
        p = [0]
        for i in x:
             if i>0:
                p [0]= i
        return p[0]


def max(lst):
	p = [-100000000000000000000000]
	for i in lst:
		if i>p[0]:
			p[0] = i
	return p[0]
def min(lst):
	p = [1000000000000000000000000]
	for i in lst:
		if i<p[0]:
			p[0] = i
	return p[0]


def frange(start, stop=None, step=None):
    # if stop and step argument is None set start=0.0 and step = 1.0
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

#    print("start= ", start, "stop= ", stop, "step= ", step)

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1
#for i in frange(0.1,0.5,0.1):
#	print (i)
#exit()
def fact(n):
	if n==0:
		return 1
	return n*fact(n-1)

def exp(x):
        y = 0
        for i in range(10):
                t = (x**i)/fact(i)
                y += t
        return y
def sin(x):
	result = 0
	for i in rnage(1,100):
		t = ((-1)**i+1)*(x**(2*i-1))/fact(2*i-1)
		result += t
	return result

def cos(x):
	result = 1
	for i in range(1,100):
		t = ((-1**i)*(x**2*i))/fact(2*i)
		result += t
	return result

def mid_point(a,b):
	return (a+b)/2

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
#		print (len(x))
		if len(x)==len(y[0]):
			for row in range(len(x)):
 #                               print (i)
				for col in range(len(y[0])):
					for col_y in range(len(y)):
						result[row][col] += x[row][col_y]*y[col_y][col]
			return result
		else:
			print("dimension not match")

def linear(x):
	return 1*x

def sigmoid(x):
	return 1/(1+exp(-x))
def derivatives_sigmoid(x):
	return x*(1-x)

def tanh(x):
	return (exp(2*x)-1)/(exp(2*x)+1)


def my_range(a,b,c=1):
	p = []
	while a<=b:
		p.append(a)
		a  += c
	return p

#print(range(1,20,.02))
#exit()

'''def equation(type,a,b,c=0):
	
	a,b,c is the paramenter of the equation
	tyep: type of equation either linear or quadratic
		case 'lin'
		cse 'qua'
	
	x = symbols('x')
	y = equation_type(type,a,b,c=0)
#	y = lambda x: 
	i_rnag = []
	t = []
	i = -100.0
	while i<=100.0:
		i_rnag.append(i)
		t1 = y.subs(x,i)
		t.append(t1)
		i += 0.01
	return t

'''
#                return result
#print(weight(2,2,4)*weight(2,2,3))
#p = weight(1,5)
#q = weight (5,1)
#print(p)
#print (q)
#t = mat_mul(p,q)
#print (t)

#p = equation.equation('lin',1,2)
#print (p)
