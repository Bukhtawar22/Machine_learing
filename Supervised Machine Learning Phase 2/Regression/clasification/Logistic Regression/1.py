from sklearn.linear_model import LogisticRegression

X = [[1],[2],[3],[4],[5]]
y = [0, 0 , 1 , 1 , 1] 

model= LogisticRegression()
model.fit(X,y)


while True:
    hours = float(input("Enter the hours: "))


    predict_result = model.predict([[hours]])[0]


    if predict_result == 1:
        print(f"Based on your hours{hours} you are passed")
    else:
        print(f"Based on your hours{hours} you are failed")
        