from my_math import *
from equation import *
from ag_nn import *

def datasets(type,a,b):
        '''
        this function is used for the generating mathematical fucntion for definiteintegral
        '''
        x = equation(type,a,b)
        integrand = x.equation()
        print ("             Your function is: {}*x+{} ".format(a,b))
        integral  = x.eq_int()
        train_x = []
        train_y = []
        m = -10
        n = 10
        for i in frange(m, n,1):
#                v_integrand = integrand(i)
                 r = random.randint(-3,3)
                 p = (i-m)/(n-m)
                 #p = sigmoid(i)
#                print (i,p)
                 v_integral = integral(i+r)
                 #q = (v_integral-0)/(integral(n)-0)
                 #q = sigmoid(v_integral)
                 train_x.append([i+r])
                 train_y.append([v_integral])
#        print (train_x)
#        p= mms.fit(train_x)
 #       p = mms.transform(train_x)
  #      q= mms.transform(train_y)
        return train_x,train_y

def main():
    # getting datasets
    print ('*************************************Hello fellow!!!**************************************************')
    print ('                   Calculating integration of linear function only f(x) = a*x+b')
    print ('                   Using parameters: ')
    print ('                        1. type = lin for linear function')
    print ('                        2. a = slope of line')
    print ('                        3. b = constant')
    print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print ("********************************************************************************************************")
    type = input("             Enter the type of function: ")
    a = int(input("             Enter the slope: "))
    b = int(input("             Enter the constant: "))
    train_x,train_y = datasets(type,a,b)
    print ("*******************************************************************************************************")
    print ("                   Provide me the upper and lower limit for integration")
    a1 = int(input("             Upper limit is: "))
    a2 = int(input("             Lower limit is: "))
    #print ((train_y[140:200]))
 #   exit()
    ##print ("+=================================================================================================")
    print("++++++++++++++++++++++++++++++++++ wait wait wait !!!! ++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    #print (train_x[140:200])
#    exit()      
    
    # create a network with one input, seven hidden neurons, two hidden layer ,and one output neurons
    n = NN(1,7,7,1)
    #n.weights()
#    exit()
    # train it with  train_x and train_y
    n.train(train_x,train_y,10000,0.0001,0.1)
    # testing
#    p1 = n.test(train_x)
    p2 = n.test([[a1],[a2]])
#    print (p2[1])
    #p3 = n.test([[(a2)]])
#    n.test(train_x[71:100])
    print ("*****************************************Thanks for waiting**************************************************")
    print ("             Result is {}".format(p2[0][0]-p2[1][0]))
    print ("***************************** one day, I will calculate the integration of all type.*********************")


if __name__ == '__main__':
    main()
