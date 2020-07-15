import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics


dataset = pd.read_csv('tsla.csv')

stock_open = dataset['High']
stock_close = dataset['Close']

x = stock_open.values.reshape(-1,1)
y = stock_close.values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train,y_train) #Training the algorithm

y_pred = regressor.predict(x_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
plt.scatter(x_test, y_test, color='gray')
plt.plot(x_test, y_pred, color='r', linewidth=2)
plt.show()
print('Mean Absoulte Error:',
        metrics.mean_absolute_error(y_test,y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

