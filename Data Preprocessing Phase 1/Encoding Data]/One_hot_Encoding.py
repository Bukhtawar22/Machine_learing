from sklearn.preprocessing import LabelEncoder
import pandas as pd 

df = pd.read_csv("sample.csv")

df_label= df.copy()
 # tool of pandas > "get.dummies" >ye text col ko binary mein convert krta hai har ek col har category ko describ kre ga

df_encoded=pd.get_dummies(df_label ,columns=['City'])
print("\nOne Hot Encoded")
print(df_encoded)