from my_math import *
class ann_structure():
	def __init__(self,in_lay, h_lay, h_neu, out_lay): 
		'''
		in_lay: input data
		h_lay : number of hidden layer
		h_neu : number of neurons in hidden layer
		out_lay : ouput
		'''
		self.in_lay = in_lay
		self.h_lay = h_lay
		self.h_neu = h_neu
		self.out_lay = out_lay

	def connection(self):
		weight = my_math.weight(self.in_lay,self.h_neu)  # define the size as per number of number of neurons in previous layer and no. of nuron in current layer
		conet1 = my_math.mat_mul(weight,in_lay)   # first layer i.e. input and firt hidden layer
		conet_layer = []
		weight_all = []
		for lay in rnage(h_lay-1):
			weight2 = my_math.weight(self.in_lay,self.h_neu)
			if lay == 0:
				con = conet1
			else:
				con = conet
			conet = my_math.mat_mul(weight2,con)                       # it will return all weight's, conet_layer_value,
			conet_layer.append(conet)
			weight_all.append(weight2)
		return weight, conet1, conet_layer, weight_all,
