from ComputeCost import computeCost
from GradientDescent import gradientDescent
from FeatureNormalize import featureNormalize
from numpy import matrix, transpose, zeros,insert
from csv import reader

with open('ex1data2.txt', 'r') as fp:
    r = reader(fp, delimiter=',')
    a = []
    b = []
    for row in r:
        [x, y, z] = int(row[0]), int(row[1]), int(row[2])
        a.append([x, y])
        b.append(z)
'''Initializing values'''
X = matrix(a)  # creating the x-data matrix
y = transpose(matrix(b))  # creating the y-data matrix
theta = zeros((3, 1))  # initializing theta value
alpha = 0.1  # initializing learning rate
num_iter = 400  # initializing no. of iterations
print('Area         No. of rooms            Cost')
for i,j in zip(X, y):
    print('%d           %d          %d'%(i[0,0],i[0,1],j[0,0]))
[X,mu,sigma]=featureNormalize(X)
X=insert(X,0,1,axis=1)
[theta, J_history] = gradientDescent(X, y, theta, alpha, num_iter)
'''Trying to predict the cost of house with sample area 1650 sq.m and 3 rooms'''
to_find=[1650,3]
normalized=(to_find-mu)/sigma
normalized=insert(normalized,0,1,axis=1)
pcost=normalized*theta
print('#########Sample Prediction#########')
print('Price of house with area %d sq.m and %d rooms is '%(to_find[0],to_find[1])),
print('$%0.2f'%pcost[0,0])
print('###################################')
'''Predicting house prices using custom inputs'''
to_find=[]
x=int(input('Enter area of house: '))
y=int(input('Enter number of rooms: '))
to_find=[x,y]
normalized=(to_find-mu)/sigma
normalized=insert(normalized,0,1,axis=1)
pcost=normalized*theta
print('Price of house with area %d sq.m and %d rooms is '%(to_find[0],to_find[1])),
print('$%0.2f'%pcost[0,0])

