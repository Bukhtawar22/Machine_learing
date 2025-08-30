from sklearn.preprocessing import StandardScaler
import pandas as pd 

scaler = StandardScaler()
X_scaled = scaler.fit_transform()
