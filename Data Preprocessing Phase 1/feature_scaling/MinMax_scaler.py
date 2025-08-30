from sklearn.preprocessing import MinMaxScaler
import pandas as pd 

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform()
