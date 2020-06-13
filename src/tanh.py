class analy_approc():
	def __init__(self, x):
		self.x = x
	def fact(self,t):
		if t == 0:
			return 1
		return  t*self.fact(t-1)
	def bernoulli(self,n):
		b = 0
		g = 0
		for k in range(n):
			for v in range(k):
				p = self.fact(k)/((self.fact(k-v)*self.fact(v)))
				p2 = ((-1)**v)*p*(v**n)
				b += p2
			j = 1/(k+1)*b
			g += j
		return g
	def tanh(self):
		p = 0.0
		for n in range(1000000):
			y = (2.0**(2*n))*((2**2*n)-1)*self.bernoulli(2*n)*(self.x**(2*n-1))
			y1 = y/self.fact(2*n)
			p += y1
		return p
	
p = analy_approc(10.0)
p1 = p.tanh()
print (p1)
