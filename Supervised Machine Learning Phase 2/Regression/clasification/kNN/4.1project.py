import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

data = pd.read_csv('cars2.csv')
df=data.copy()
le = LabelEncoder()
df['Make Encoded']=le.fit_transform(df['Make'])



X =df[["Max Price","Year"]]
y=df['Make Encoded']



model=KNeighborsClassifier(n_neighbors=1)
model.fit(X,y)

while True:
    user_price = int(input("Enter cars price: "))
    user_year = int(input("Enter cars year: "))

    pred_encoded=model.predict([[user_price ,user_year]])[0]


    car_name=le.inverse_transform([pred_encoded])[0]
    print(f"Prediction car name: {car_name} and for price: {user_price} , for year {user_year}")





