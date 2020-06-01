import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("heightweight.csv")

x = df.iloc[: ,[0 ,1]].values

MODEL = KMeans(n_clusters = 7)
MODEL.fit(x)

y = MODEL.predict(x)
print(y)
