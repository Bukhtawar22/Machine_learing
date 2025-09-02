'''''
text ko number mein convert krta hai jesie
yes > 1
no > 0
or ye bs 2 number pr hi kam krta hai 
2 value pr kam krta hai
lebal encoder string ko number ban dyga
'''
from sklearn.preprocessing import LabelEncoder
import pandas as pd 

df = pd.read_csv("sample.csv")

df_label= df.copy()

le= LabelEncoder()

df_label['Gander_Encoded']=le.fit_transform(df_label['Gander'] )
df_label['Passed_Encoded']=le.fit_transform(df_label['Passed'])

print("\nLabel Encoed Data")
print(df_label[['Name','Gander','Gander_Encoded','Passed','Passed_Encoded']].head())

