from sklearn.neighbors import KNeighborsClassifier
import pandas as pd 

X =  [[180 , 7],[200,7.5],[250 ,8],[300 ,8.5],[330 ,9],[360 ,9.5]]

# 0 = Apple , 1 = orange

y = [0,0,0,1,1,1]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)
weight= float(input("Enter the weight in gm"))
size= float(input("Enter the size in cm"))

prediction = model.predict([[weight,size]])[0]
#[0]->
if prediction ==0:
    print("this is likly an apply",prediction)

else:
    print("this is an orange")