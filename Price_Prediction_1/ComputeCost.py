import numpy
def computeCost(X,y,theta):
    m=len(y) #no. of training examples
    J=0 #initialize cost
    Xt=numpy.transpose(X)
    J=sum((1/(2*m))*numpy.square((X*theta)-y))
    return J

