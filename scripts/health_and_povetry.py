import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('../datasets/HealthAndPoverty_Data.csv',sep=';')
health_and_povetry_brasil = dataset[dataset.CountryCode.eq("BRA")]
adolescent_fertility_brasil = health_and_povetry_brasil[health_and_povetry_brasil.SeriesCode.eq("SP.ADO.TFRT")]
adolescent_fertility_brasil_2018 = adolescent_fertility_brasil[adolescent_fertility_brasil.Year < 2019]
X = adolescent_fertility_brasil_2018.iloc[:, 4:-1].values
y = adolescent_fertility_brasil_2018.iloc[:, 5].values
print(adolescent_fertility_brasil_2018.iloc[:, 4:-1].values)
print(adolescent_fertility_brasil_2018.iloc[:, 5].values)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Adolescent fertility rate in Brazil ')
plt.xlabel('Fertility rate')
plt.ylabel('Years')
plt.show()