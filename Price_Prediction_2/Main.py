from numpy import matrix, transpose, insert
from csv import reader
from NormalEquation import normalEquation

with open('ex1data2.txt', 'r') as fp:
    r = reader(fp, delimiter=',')
    a = []
    b = []
    for row in r:
        [x, y, z] = int(row[0]), int(row[1]), int(row[2])
        a.append([x, y])
        b.append(z)
X = matrix(a)
X = insert(X, 0, 1, 1)
y = transpose(matrix(b))
theta = normalEquation(X, y)
'''Predicting cost of an example set: Area=1650 sq.m and no.of rooms:3'''
to_find = [1,1650, 3]   #Extra '1' appended for calculation purpose[see readme for reference]
pcost = to_find * theta
print('#########Sample Prediction#########')
print('Price of house with area %d sq.m and %d rooms is ' % (to_find[0], to_find[1])),
print('$%0.2f' % pcost[0, 0])
print('###################################')
'''Predicting house prices using custom inputs'''
to_find = []
x = int(input('Enter area of house: '))
y = int(input('Enter number of rooms: '))
to_find = [1,x, y]  #Extra '1' appended for calculation purpose[see readme for reference]
pcost = to_find * theta
print('Price of house with area %d sq.m and %d rooms is ' % (to_find[0], to_find[1])),
print('$%0.2f' % pcost[0, 0])
