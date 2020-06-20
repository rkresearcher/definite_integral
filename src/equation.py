from my_math import *
#import math
class equation:
	def __init__(self,type,a,b=0,c=0):
		self.type = type
		self.a = a
		self.b = b
		self.c = c
	def equation(self):	
		if self.type == 'lin':
			y = lambda x: self.a*x+self.b
		elif self.type == 't_sin':
			y = lambda x:self.a*sin(x)
		elif self.type == 'qua':
			y = lambda x: self.a*(x**2)+self.b*x+self.c
		elif self.type == 'exp':
			y = lambda x: exp(self.a*x)
		elif self.type == 'tri':
			y = lambda x: self.a*(x**3)
		elif self.type == 'for':
			y = lambda x: self.a*(x**4)
		elif self.type == 'fiv':
        	        y = lambda x: self.a*(x**5)
		elif self.type == 'six':
       		        y = lambda x: self.a*(x**6)
		elif self.type == 'sev':
	                y = lambda x: self.a*(x**7)
		elif self.type == 'eig':
        	        y = lambda x: self.a*(x**8)
		elif self.type == 'nin':
       		        y = lambda x: self.a*(x**9)
		elif self.type == 'ten':
       		        y = lambda x: self.a*(x**10)
		elif self.type == 'ele':
       		        y = lambda x: self.a*(x**11)
		elif self.type == 'twe':
      		        y = lambda x: self.a*(x**12)
		elif self.type == 'thir':
	                y = lambda x: self.a*(x**13)
		elif self.type == 'fourt':
        	        y = lambda x: self.a*(x**14)
		elif self.type == 'fift':
	                y = lambda x: self.a*(x**15)
		elif self.type == 'sixt':
	                y = lambda x: self.a*(x**16)
		elif self.type == 'sevet':
	                y = lambda x: self.a*(x**17)
		elif self.type == 'eight':
	                y = lambda x: self.a*(x**18)
		elif self.type == 'nint':
	                y = lambda x: self.a*(x**19)
		elif self.type == 'twen':
	                y = lambda x: self.a*(x**20)
		elif self.type == 'tweno':
	                y = lambda x: self.a*(x**21)
		elif self.type == 'twent':
	                y = lambda x: self.a*(x**22)
		elif self.type == 'twenth':
	                y = lambda x: self.a*(x**23)
		elif self.type == 'twenf':
	                y = lambda x: self.a*(x**24)
		elif self.type == 'twenfi':
        	        y = lambda x: self.a*(x**25)
		elif self.type == 'twensi':
	                y = lambda x: self.a*(x**26)
		elif self.type == 'twense':
	                y = lambda x: self.a*(x**27)
		elif self.type == 'twenei':
	                y = lambda x: self.a*(x**28)
		return y


	def eq_int(self):
			
		if self.type == 'lin':
			y = lambda x: (self.a*(x**2))/2+self.b*x
		elif self.type == 't_sin':
			y = lambda x:self.a*cos(x)
		elif self.type == 'qua':
			y = lambda x: self.a*(x**3)/3+self.b*(x**2)/2+self.c*x
		elif self.type == 'exp':
			y = lambda x: self.a*exp(self.a*x)
		elif self.type == 'tri':
			y = lambda x: self.a*(x**4)/4
		elif self.type == 'for':
			y = lambda x: self.a*(x**5)/5
		elif self.type == 'fiv':
        	        y = lambda x: self.a*(x**6)/6
		elif self.type == 'six':
       		        y = lambda x: self.a*(x**7)/7
		elif self.type == 'sev':
	                y = lambda x: self.a*(x**8)/8
		elif self.type == 'eig':
        	        y = lambda x: self.a*(x**9)/9
		elif self.type == 'nin':
       		        y = lambda x: self.a*(x**10)/10
		elif self.type == 'ten':
       		        y = lambda x: self.a*(x**11)/11
		elif self.type == 'ele':
       		        y = lambda x: self.a*(x**12)/12
		elif self.type == 'twe':
      		        y = lambda x: self.a*(x**13)/13
		elif self.type == 'thir':
	                y = lambda x: self.a*(x**14)/14
		elif self.type == 'fourt':
        	        y = lambda x: self.a*(x**15)/15
		elif self.type == 'fift':
	                y = lambda x: self.a*(x**16)/16
		elif self.type == 'sixt':
	                y = lambda x: self.a*(x**17)/17
		elif self.type == 'sevet':
	                y = lambda x: self.a*(x**18)/18
		elif self.type == 'eight':
	                y = lambda x: self.a*(x**19)/19
		elif self.type == 'nint':
	                y = lambda x: self.a*(x**20)/20
		elif self.type == 'twen':
	                y = lambda x: self.a*(x**21)/21
		elif self.type == 'tweno':
	                y = lambda x: self.a*(x**22)/22
		elif self.type == 'twent':
	                y = lambda x: self.a*(x**23)/23
		elif self.type == 'twenth':
	                y = lambda x: self.a*(x**24)/24
		elif self.type == 'twenf':
	                y = lambda x: self.a*(x**25)/25
		elif self.type == 'twenfi':
        	        y = lambda x: self.a*(x**26)/26
		elif self.type == 'twensi':
	                y = lambda x: self.a*(x**27)/27
		elif self.type == 'twense':
	                y = lambda x: self.a*(x**28)/28
		elif self.type == 'twenei':
	                y = lambda x: self.a*(x**29)/29
		return y



