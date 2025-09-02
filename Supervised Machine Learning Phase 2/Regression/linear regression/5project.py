''' for students hours based marks project '''

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error

data = pd.read_csv('score.csv')
print(data)
X = data[['Hours']]
y=data['Scores']

X_train ,X_test ,y_train ,y_test = train_test_split(X,y , test_size=0.2 , random_state=42)

print("X Train")
print(X_train)

print("y_train")
print(y_train)

print("X test")
print(X_test)

print("y test")
print(y_test)
'''
Evaluation (MAE, MSE, RMSE) sirf 2 cheezon ke darmiyan hota hai:

y_test → asal (real / ground truth answers)

y_pred → jo model ne predict kiya

⚠️ Tum pehle X aur y de rahe the, jo galat tha (kyunki X inputs hain, predictions nahi).
'''


model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)




plt.scatter(X_train, y_train, color="blue", label="Train data")
plt.scatter(X_test, y_test, color="green", label="Test data")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Prediction Line")
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.legend()
plt.show()
