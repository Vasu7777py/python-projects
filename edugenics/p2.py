import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

#to scale
from sklearn.preprocessing import StandardScaler

#for splitting data into tranning and testing values
from sklearn.model_selection import train_test_split

#importing data
df = pd.read_csv("Social_Network_Ads.csv")

ENC = LabelEncoder()
STD = StandardScaler()
MODEL = LogisticRegression()

# transforming str to numeric understandable by computer
ENC.fit(df.Gender)
df.Gender = ENC.transform(df.Gender)

#i/o
x = df.iloc[:,[2,3]].values
y = df.iloc[:,4].values

#splitting data into tranning and testing values
x_train ,x_test ,y_train ,y_test = train_test_split(x , y ,random_state = 0)

# to transform the existing data which has large variation 
# into data which has less variation 
x_train = STD.fit_transform(x_train)
x_test = STD.fit_transform(x_test)

MODEL.fit(x_train ,y_train)

#predicting
Predict = MODEL.predict(x_test)
print(Predict , "\n",y_test)

#finding effe
print(MODEL.score(x_test ,y_test)*100)
