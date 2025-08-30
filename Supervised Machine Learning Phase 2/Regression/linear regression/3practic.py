from sklearn.linear_model import LinearRegression
import pandas as pd 

#Practice

df = pd.read_csv('study.csv')


# Features (X) aur Target (y) alag karo
X = df[['Hours']]   # Double brackets lagane ka matlab dataframe format me rakhna
y = df['Marks']     # Single bracket se Series milegi


#model train

model = LinearRegression()

model.fit(X,y)

while True:

        # user sy input ly kr prediction

        hour = float(input("Enter hours which u wanna study: "))

        prediction= model.predict([[hour]])[0]


        if hour <= 2 :
            print(f"Based on your hour {hour}, you may score around {prediction} u will fail")
        else:
            print(f"Based on your hour {hour}, you may score around {prediction} u will passed")
      


