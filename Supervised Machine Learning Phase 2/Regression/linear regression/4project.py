import pandas as pd 

data = pd.read_csv('cars price pakistan.csv')
print(data.info())

# convert into int
data['Min Price']=data['Min Price'].str.replace(',','').astype(int)
data['Max Price']=data['Max Price'].str.replace(',','').astype(int)
print(data.info())

data.to_csv('cars.csv', index=False)

