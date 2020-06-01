import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

std = MinMaxScaler()
MODEL = LogisticRegression()
MODEL2 = DecisionTreeClassifier()
df = pd.read_csv("fruit_data_with_colors.txt" ,sep = "\t")
Fruit_name = df.fruit_name.unique()
Fruit_size = df.groupby("fruit_name" ,sort = False).size()
x = df.iloc[: ,[3 ,4 ,5 ,6]].values
y = df.iloc[: ,[1]].values

x_train ,x_test ,y_train ,y_test = train_test_split(x ,y ,random_state = 0)
x_train = std.fit_transform(x_train)
x_test = std.fit_transform(x_test)

MODEL.fit(x_train ,y_train)
pred = MODEL.predict(x_test)
print(pred)
print(MODEL.score(x_test ,y_test)*100)
MODEL2.fit(x_train ,y_train)
print(MODEL2.score(x_test ,y_test)*100)