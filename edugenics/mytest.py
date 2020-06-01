import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("diabetes.csv")

#x = df.iloc[: ,[0, 1 ,2 ,3 ,4 ,5 ,6 ,7]].values
x = df.iloc[: ,1].values
z = df.iloc[: ,2].values
w = df.iloc[: ,4].values
y = df.iloc[: ,[8]].values

#plt.scatter(x ,y)
#plt.scatter(z ,y)
plt.scatter(w ,y)
plt.show()