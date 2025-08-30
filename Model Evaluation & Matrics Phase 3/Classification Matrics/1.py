from sklearn.metrics import accuracy_score , precision_score,recall_score,f1_score

#True answer (what actually happened)
y_true = [1,0,1,1,0,1,0]

#model prediction (what is gussed)
y_pred=[1,0,1,0,0,1,1]

#evaluation

print("Accuracy:" , accuracy_score(y_true , y_pred))
print("precision:" , precision_score(y_true , y_pred))
print("Recall:" , recall_score(y_true , y_pred))
print("F1 Score:" , f1_score(y_true , y_pred))
