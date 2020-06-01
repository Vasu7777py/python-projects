import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

std = StandardScaler()
MODEL = DecisionTreeClassifier()

df = pd.read_csv("diabetes.csv")

x = df.iloc[: ,[0, 1 ,2 ,3 ,4 ,5 ,6 ,7]].values
y = df.iloc[: ,[8]].values

x_train ,x_test ,y_train ,y_test = train_test_split(x ,y ,random_state = 0)
x_train = std.fit_transform(x_train)
x_test = std.fit_transform(x_test)

MODEL.fit(x_train ,y_train)

pred = MODEL.predict(x_test)
print(pred)
print(MODEL.score(x_test ,y_test)*100)
#print(accuracy_score(y_train ,pred)*100)
