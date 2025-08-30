from sklearn.linear_model import LogisticRegression
import pandas as pd 
 #Practice
df = pd.read_csv('yes_no.csv')

X = df[['Marks']]
y = df['Status']

model = LogisticRegression()
model.fit(X,y)


while True:
    marks = float(input("Enter your marks:  "))
    prediction = model.predict([[marks]])


    if prediction == 1  and marks <= 200:
        print(f"Based on you are Marks {marks} you are {prediction} PASSED!")
    elif prediction == 0:
        print(f"Based on you are Marks {marks} you are {prediction} FAILED!")
    else:
        print(f" Based on out of 200 marks only")

        
        