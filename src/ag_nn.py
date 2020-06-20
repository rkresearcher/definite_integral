import random
from equation import *
from my_math import *
random.seed(0)
# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
#    return tanh(x)
#     return x/1000000
#    return 1/(1+math.exp(-x))
     return max([x])
#      return x

# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    #return 1.0-y**2
#     return 2
#    return y*(1-y)
     if y>0:
          return 1
     else:
          return 0
def dsigmoidp(y):
    return 1
#     return 1
#    return y*(1-y)

class NN:
    def __init__(self, ni, nh, nh1 ,no):
        # number of input, hidden_layer one, hidden layer two and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh = nh
        self.nh1 = nh1
        self.no = no

        # activations for nodes
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ah1 =[1.0]*self.nh1
        self.ao = [1.0]*self.no

        # create weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wi1 = makeMatrix(self.nh,self.nh1)
        self.wo = makeMatrix(self.nh1, self.no)
        # set them to random vaules

        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(0.02, 0.020)
        for i in range(self.nh):
            for j in range(self.nh1):
                self.wi1[i][j] = rand(0.002,0.0020)
        for j in range(self.nh1):
            for k in range(self.no):
                self.wo[j][k] = rand(-0.2, 0.2)

        # last change in weights for momentum
        self.ci = makeMatrix(self.ni, self.nh)
        self.ci1 = makeMatrix(self.nh,self.nh1)
        self.co = makeMatrix(self.nh1, self.no)

    def update(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni-1):
           # print (i)
#            print (inputs[i])
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]


        # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(sum)

        #hidden1 activations
        for j in range(self.nh1):
            sum = 0.0
            for i in range(self.nh):
                sum = sum + self.ah[i] * self.wi1[i][j]
            self.ah1[j] = sigmoid(sum)

        # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh1):
                sum = sum + self.ah1[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:]

    def pred(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni-1):
           # print (i)
#            print (inputs[i])
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]
     # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(sum)

        #hidden1 activations
        for j in range(self.nh1):
            sum = 0.0
            for i in range(self.nh):
                sum = sum + self.ah[i] * self.wi1[i][j]
            self.ah1[j] = sigmoid(sum)
     # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh1):
                sum = sum + self.ah1[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:]


    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
#            print (targets[k])
            error = targets[k]-self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error
       # print (self.ah1)
 #       print (self.ah)

        # calculate error terms for hidden1
        hidden_deltas1 = [0.0] * self.nh1
        for j in range(self.nh1):
            error = 0.0
            for k in range(self.no):
                error = error + output_deltas[k]*self.wo[j][k]
            hidden_deltas1[j] = dsigmoid(self.ah1[j]) * error

	# calculate error terms for hidden 
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.nh1):
                error = error + hidden_deltas1[k]*self.wi1[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # update output weights
        for j in range(self.nh1):
            for k in range(self.no):
                change = output_deltas[k]*self.ah1[j]
                self.wo[j][k] = self.wo[j][k] + N*change #+ M*self.co[j][k]
                self.co[j][k] = change
                #print N*change, M*self.co[j][k]
        # update hidden1 layer weight
        for j in range(self.nh):
            for k in range(self.nh1):
                change = hidden_deltas1[k]*self.ah[j]
                self.wi1[j][k] = self.wi1[j][k] + N*change #+ M*self.ci1[j][k]
                self.ci1[j][k] = change

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N*change + M*self.ci[i][j]
                self.ci[i][j] = change


        # calculate error
        error = 0.0
        for k in range(len(targets)):
            self.ao[k]
#            error = 0.99
            error += 0.5*(targets[k]-self.ao[k])**2
        return error,self.wi,self.wi1,self.wo


    def test(self, inputs):
        #print (self.wo)
        #print (self.wi1)
        #print (self.wi)
       # for i in range(len(inputs)):
            g = []
            for p in inputs:
                 g.append(self.update(p))
#                print(p, '->', self.update(p))
            return g

    def weights(self):
        print('Input weights:')
        for i in range(self.ni):
      #      print(i)
            print(self.wi[i])
        print('=================================')

        for i in range(self.nh1):
            print(self.wi1[i])
        print('+++++++++++++++++++++++++++++++++')

        print('Output weights:')
        for j in range(self.nh):
            print(self.wo[j])

    def train(self, train_x, train_y, iterations=10000, N=0.1, M=1):
        # N: learning rate
        # M: momentum factor
	# lenght of train_x and train_y are equal
        #error = 0.0
  #        while (p):
            for w in range(len(train_y)-4):  
               r = random.randint(-2,2,)
               for i in range(iterations):
                    error = 0.0
                    for p,q in zip ([train_x],[train_y]):
                        inputs = p[9]
#                        print (p[w])
#                       exit()
                        targets = q[9]
 #                       print (targets[w])
#                       exit()
                        z = self.update(inputs)
                        error1,wi,wi1,wo = self.backPropagate(targets, N, M)
                        error += error1 
                        '''if i % 1000 == 0:
                            #self.weights()
                            print('wwwwwwwwwwwwwwwwwwwiiiiiiiiiiiiiiiiiiiwwwwwwwwwwwwwwwwwwwwwiiiiiiiiiiiiiiiiiiiii')
                            print(wi)
                            print ('wwwwwwwwwwwwwwwwwwwiiiiiiiiiiiiiiiiiii11111111111111111wwwwwwwwwwwwwwwwwiiiiiii111')
                            print(wi1)
                            print('wwwwwwwwwwwwwwwwwwwwwwwooooooooooooooooooooooooowwwwwwwwwwwwwwwwwwwwwwwwwwwwoooooooo')
                            print(wo)
                            print('error {} after iteration {} {} {}, actula output is: {}'.format(error,i,p[w],q[w],z))'''
                        '''if error < 0.001:
                            break
                    else:
                        continue
                    break
               else:
                    continue
               break'''              


