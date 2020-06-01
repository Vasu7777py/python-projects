import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

#importing data
df = pd.read_csv("fruits.csv")

ENC = LabelEncoder()

# transforming str to numeric understandable by computer
ENC.fit(df.Color)
df.Color = ENC.transform(df.Color)

MODEL = LogisticRegression()

# i/o 
x = df.iloc[:,[0,1]].values
y = df.iloc[:,2].values

MODEL.fit(x,y)

#predicting
y_pred = MODEL.predict([[2,11]])
print(y_pred)
print(MODEL.score(x ,y)*100)
