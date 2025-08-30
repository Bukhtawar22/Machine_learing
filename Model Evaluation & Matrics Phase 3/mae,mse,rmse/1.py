''''
MAE
1- take the mistake difference
2- remove the minus sign
3- add
4- divide

7.5 on average

MSE 


1- square every mistake value
2-add
3- divide total

RMSE
Root Mean squared error
'''
from sklearn.metrics import mean_absolute_error , mean_squared_error
import numpy as np

#real scores
real_score = [90,60,80,100]
# model guess
predicted_score = [85,70,70,95]

mae = mean_absolute_error(real_score,predicted_score)
mse = mean_squared_error(real_score,predicted_score)
rmse =np.sqrt(mse)

print("MAE on Average off by:",mae)
print("MSe on Squared mistake value:",mse)
print("Rmse final realistic error:",rmse)