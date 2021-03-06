import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

dataset = pd.read_csv('../datasets/insurance.csv')


X = dataset.iloc[:, :-6].values
y = dataset.iloc[:, 6].values
print(dataset.iloc[:, :-6].values)
print(dataset.iloc[:, 6].values)


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
plt.title('Age vs Insurance charges')
plt.xlabel('Age')
plt.ylabel('Insurance charges')
plt.show()
