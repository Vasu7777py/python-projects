# Name :- Vasu.Subbannavar
# Email :- subbannavarvasu@gamil.com
# mobile no :- 7899927254

# Date :- 28/02/2020
# Topic :- Heart Disease UCI
# Database name :- heart.csv
# source :- Internet

# importing requried modules for ML programing
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

STD = StandardScaler()
MODEL = RandomForestClassifier( n_estimators = 13,max_depth = 10 ,max_leaf_nodes = 13 ,warm_start = True)

# creating a data frame using a panda module
Heart_DF = pd.read_csv("heart.csv")

# age       [0]     i/p
# sex       [1]     i/p
# cp        [2]     i/p
# trestbps  [3]     i/p
# chol      [4]     i/p
# fbs       [5]     i/p
# restecg   [6]     i/p
# thalach   [7]     i/p
# exang     [8]     i/p
# oldpeak   [9]     i/p
# slope     [10]    i/p
# ca        [11]    i/p
# thal      [12]    i/p

# target    [13]    o/p

# taking data from data frame and creating a list of input and outupt
x = Heart_DF.iloc[: ,[0 ,1 ,2 ,3 ,4 ,5, 6 ,7 ,8 ,9 ,10 ,11 ,12 ]]
y = Heart_DF.iloc[: ,[13]]

# to transform the existing data which has large variation into data which has less variation
x = STD.fit_transform(x)

# spliting the input data into test and train data
x_train ,x_test ,y_train ,y_test = train_test_split(x , y)

# creating a MODEL using trainig data, using this trainig data the model trains its self for excepting
# unexpected or random data and predicts an output
# << IN THSI CASE THE OUTPUT IS WETEHR A PRESON HAS A HEART PROBLEM OR NOT!! >>
# << 1 = there is a problem ,and 0 = there is no problem >>
MODEL.fit(x_train ,y_train)

# the model is predecting for new data and displaying the accrucy in "%"
print(MODEL.predict(x_test) ,MODEL.score(x_test ,y_test)*100)