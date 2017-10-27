import numpy
from ComputeCost import computeCost
def gradientDescent(X, y, theta, alpha, num_iter):
    m = len(y)  # number of training examples
    J_history = numpy.zeros((num_iter, 1))
    Xt = numpy.transpose(X)
    for i in range(num_iter):
        theta = theta - ((alpha / m) * (numpy.transpose(numpy.transpose((X * theta) - y) * X)))  # performing gradient step
        J_history[i] = computeCost(X, y, theta)  # computing cost function

    return [theta,J_history]
