import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
    
def validateNumberRange(ds, column, min, max): 
    ds = dataset[column].describe()
    if ds["min"] < min :
        print("Invalid dataset value: wrong input for column: " + column + "")
    if ds["max"] > max :
        print("Invalid dataset value: Record input for column: " + column + ": " + str(ds["max"]) + " transpasses the maximum allowed : " + str(max))


#read dataset
dataset = pd.read_csv('../datasets/insurance.csv')

#Get records length 
recordsLenght = len(dataset)

# Drops null values
dataset.dropna(inplace = True)

#Validate age values
validateNumberRange(dataset, "age", 0, 130)
dataset["age"].describe() 
if ["min"] < 18:  
        print("Warning: Potential implications and risks for records on column: " + "age" + ", value: " + str(ds["min"]))
validateNumberRange(dataset, "bmi", 0, 150)
validateNumberRange(dataset, "charges", 0, 100000)



