import pandas as pd 
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

''''
koi chiz khud sy sik kr impliment krna hoga model ko
isly hum data ko splite krty hein take  vo new questions pr bhi kam krpayty
unseen data pr test krpay
'''
datas = {
    'studying':[1,2,3,4,5],
    'testscore':[40,50,60,70,80]
}
df = pd.DataFrame(datas)



#standard scaler///////
standard_scaler = StandardScaler()

standard_scaled=standard_scaler.fit_transform(df)

print("Standard Scaler output")
print(pd.DataFrame(standard_scaled, columns=['Gender','testscore']))


minmax_scaler = MinMaxScaler()
minmax_scaler =minmax_scaler.fit_transform(df)

print("min max output")
print(pd.DataFrame(minmax_scaler,columns=['studying','testscore']))



X = df[['studying']]
y=df[['testscore']]
 
X_train , X_test , y_train ,y_test=train_test_split(X ,y , test_size=0.2, random_state=42)

print("Training data")
print(X_train)

print("Test data")
print(X_test)

print("Training data")
print(y_train)

print("Test data")
print(y_test)