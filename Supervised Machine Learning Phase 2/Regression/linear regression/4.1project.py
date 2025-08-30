import pandas as pd 
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('cars.csv')
print(data.info())


# Frequency of each model
print(data['Make'].value_counts())

data_label=data.copy()
le = LabelEncoder()

data_label['Make Encoded']=le.fit_transform(data_label['Make'])
data_label['Model Encoded']=le.fit_transform(data_label['Model'])
print("\n Encoded label")
# print(data_label[['Make','Make Encoded','Model','Model Encoded']].to_string())
# print(data_label[['Make',"Make Encoded"]].to_string())

# print(data_label[['Make Encoded','Max Price']].to_string())
