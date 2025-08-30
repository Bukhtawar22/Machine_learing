from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error
import pandas as pd
import numpy as np 

data =pd.read_csv('marks.csv')

X = data[['Hours']]
y =data['Marks']

model = LinearRegression()

model.fit(X,y)

predicted_marks= model.predict(X)

#evaluate
mae = mean_absolute_error(y ,predicted_marks)
mse = mean_squared_error(y ,predicted_marks)
rmse = np.sqrt(mse)

#show result

print("MAE:", mae)
print("MsE:", mse)
print("RMSE:", rmse)


new_predict = model.predict([[7]])

print(f"Prediction for 7 h ours is marks {new_predict}")

