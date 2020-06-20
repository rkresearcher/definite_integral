from my_math import *
class approximation():
	def __init__(self,function,a,b,n=7):
		'''
		function = input function or we can say integrand
		a = lower limit of the interval
		b = upper limit of the interval
		'''
		self.function = function
		self.a = a
		self.b = b
		self.n = n
	def midpoint(self):

		h = float(self.b-self.a)/self.n
		result = 0
		for i in range(self.n):
			result += self.function((self.a + h/2.0) + i*h)
		result *= h
		return result
	def trapezoidal(self):
		h = float(self.b-self.a)/self.n
		result = 0.5*self.function(self.a) + 0.5*self.function(self.b)
		for i in range(1, self.n):
			result += self.function(self.a + i*h)
		result *= h
		return result
	def tanh(self):
		h = float(self.b-self.a)/self.n
		result = 0
		for i in range(self.n):
			result += tanh(h/2*self.function(self.a+h/2.0+i*h))

		result *= 2
		return result

