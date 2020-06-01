import pandas as pd
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("areavsprice.csv")
MODEL = LinearRegression()

plt.scatter(df.Area ,df.Price ,marker = "*")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

x = df.iloc[: ,[0]].values
y = df.iloc[: ,[1]].values

MODEL.fit(x ,y)
pred = MODEL.predict([[87576]])
print(pred)
