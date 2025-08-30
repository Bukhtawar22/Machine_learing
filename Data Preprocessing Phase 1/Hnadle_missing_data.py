import pandas as pd

data ={
    "Name":['fahad','bk','bukhtawar','ali'],
    "Age":[27,None,28,30],
    "Salary":[5500,5000,None,80000],
}

df= pd.DataFrame(data)
print("Orignal datafra,")
print(df)

print(df.isnull().sum())
print('in precentage')
print(df.isnull().mean()*100)
df_drop =df.dropna()
print(df_drop)

# df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Age'].mean())

# df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)