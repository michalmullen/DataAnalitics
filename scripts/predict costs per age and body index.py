import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sys

def square(n): 
    return n * n 

dataset = pd.read_csv('../datasets/insurance.csv')
X1 = dataset.iloc[:, 0].values
X2 = dataset.iloc[:, 2].values
y = dataset.iloc[:, 6].values

len = len(X1)
sumSquareX1 = sum(map(square, X1)) 
sumSquareX2 = sum(map(square, X2)) 

sumX1Y = 0
for i, j in zip(X1, y):
    sumX1Y += i*j

sumX2Y = 0
for i, j in zip(X2, y):
    sumX2Y += i*j
    
sumX1X2 = 0
for i, j in zip(X1, X2):
    sumX1X2 += i*j
    
sumX1 = sum(X1)

sumX2 = sum(X2)

sumY = sum(y)

sumSquareX1 = sumSquareX1 - ((sumX1 * sumX1) / len)

sumSquareX2 = sumSquareX2 - ((sumX2 * sumX2) / len)

sumX1Y = sumX1Y - ((sumX1 * sumY) / len)

sumX2Y = sumX2Y - ((sumX2 * sumY) / len)

sumX1X2 = sumX1X2 - ((sumX1 * sumX2) / len)

b1 = (sumSquareX2 * sumX1Y - sumX1X2 * sumX2Y) / ((sumSquareX1 * sumSquareX2) - (sumX1X2 * sumX1X2))

b2 = (sumSquareX1 * sumX2Y - sumX1X2 * sumX1Y) / ((sumSquareX1 * sumSquareX2) - (sumX1X2 * sumX1X2))

b0 = (sumY / len) - (b1 * (sumX1 / len)) - (b2 * (sumX2 / len))

cost = b0 + b1 * float(sys.argv[1]) + b2 * float(sys.argv[2])

print("coeficient intercept: " + str(b0))
print("coeficient age: " + str(b1))
print("coeficient bmi: " + str(b2)  )

print("The expected insurance costs for a " + sys.argv[1] + " years old customer with body mass index of " + sys.argv[2] + " is: " + str(cost))

