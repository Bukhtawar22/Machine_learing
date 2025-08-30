from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
y = [40, 50, 65, 75, 90]


model =LinearRegression()
model.fit(X,y)

hours = float(input("Enter how many hours: "))

predicted_marks=model.predict([[hours]])[0]
print(f"Based on your hour {hours} your may score around {predicted_marks} ")

''''
impotants 

1- its not about the line , its about the story
2- 5 row use start
3- accuracy is not always the goal 

'''