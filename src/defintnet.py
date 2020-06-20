from equation import *
from approximation_layer import *

y = equation('lin',2)
up_lim = -8
low_lim = -2

def first_lay(y=y,up_lim=up_lim,low_lim=low_lim):
	approx = approximation(y,up_lim,low_lim)
	approx1 = approx.midpoint()
	approx2 = approx.trapezoidal()
	approx3 = approx.tanh()
#	return [approx1,approx2,approx3]
	print (approx1)
	print (approx2)
	print (approx3)
first_lay()
