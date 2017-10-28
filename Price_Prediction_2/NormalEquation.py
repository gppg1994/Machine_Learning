from numpy import transpose,zeros
from numpy.linalg import pinv


def normalEquation(X, y):
    cols=X.size/len(X)
    theta=zeros((int(cols),1))
    A = (transpose(X) * X)
    theta = (pinv(A) * transpose(X)) * y  # Calculating theta value according to Normal Equation
    return theta
