from matplotlib import pyplot as plt

data = [26 ,75 ,100 ,66 ,77]
languangs = ["c++" ,"c" ,"Python" ,"Java" ,"c#"]
exp = [0 ,0 ,0 ,0 ,0]

plt.pie(data ,exp ,languangs)
plt.show()