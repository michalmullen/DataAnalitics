import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

def square(n): 
    return n * n 

dataset = pd.read_csv('../datasets/insurance.csv')
X = dataset.iloc[:, 0].values
y = dataset.iloc[:, 6].values

len = len(X)
sumX = sum(X)
sumY = sum(y)
sumSquareX = sum(map(square, X)) 
sumSquareY = sum(map(square, y)) 

sumXY = 0
for i, j in zip(X, y):
    sumXY += i*j

a = (sumY * sumSquareX - sumX * sumXY) /  (len * sumSquareX - sumX * sumX)

b = (len * sumXY - sumX * sumY) / (len * sumSquareX - sumX * sumX)


cost = a + b * float(sys.argv[1])


print("coeficient intercept: " + str(a))
print("coeficient age: " + str(b))

print("The expected insurance costs for a " + sys.argv[1] + " years old customer is: " + str(cost))

