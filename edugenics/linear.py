import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

df  = pd.read_csv("SPORTS.csv")

MODEL_LOGIC = LogisticRegression()
MODEL_RAND = RandomForestClassifier(max_depth = 3)
MODEL_TREE = DecisionTreeClassifier()

x = df.iloc[: ,[1 ,2 ,3]].values
y = df.iloc[:, [0]].values

MODEL_LOGIC.fit(x ,y)
MODEL_RAND.fit(x ,y)
MODEL_TREE.fit(x ,y)

pred_logic = MODEL_LOGIC.predict(x)
pred_rand = MODEL_RAND.predict(x)
pred_tree = MODEL_TREE.predict(x)

print("pred_logic"  + str(MODEL_LOGIC.score(x ,y)*100))
print("pred_rand" + str(MODEL_RAND.score(x ,y)*100))
print("pred_tree" + str(MODEL_TREE.score(x ,pred_tree)*100))
