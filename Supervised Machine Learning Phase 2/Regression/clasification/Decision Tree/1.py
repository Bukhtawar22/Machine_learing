from sklearn.tree import DecisionTreeClassifier

X = [[7,2],[8,2],[9,8],[10,9]]
y=[0,0,1,1]
# 0 = Apple , 1 = orange

model =DecisionTreeClassifier()
model.fit(X,y)

size= float(input("Enter the fruit size in  cm"))
shade= float(input("Enter the color shade (1 - 10)  "))

prediction = model.predict([[size,shade]])[0]

if prediction == 0:
    print("this is likly Apply")
else:
    print("this is likly orange")