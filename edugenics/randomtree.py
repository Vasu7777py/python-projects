import pandas as pd
from sklearn import datasets

iris = datasets.load_iris
print(iris.__getattribute__(datasets))
print(iris)