import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

MODEL = KNeighborsClassifier(n_neighbors = 3 ,metric = "euclidean")
df = pd.read_csv("weight-knn.csv")

x = df.iloc[: ,[0,1]].values
y = df.iloc[: ,2].values

MODEL.fit(x ,y)
print(MODEL.predict([[45 ,330]]))
print(MODEL.score(x ,y)*100)