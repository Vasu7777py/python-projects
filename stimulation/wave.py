from matplotlib import pyplot as plt
import numpy as np

import utility.math as math


A = 7
W = 7
phi = 9
K = 5

#Y(x, t) = A * sin(Kx - Wt + phi)
x = 0
Y_Plt = []
X_Plt = []
T_Plt = []
t = 0

def Wave(x, t):
	Y = (A * np.sin(math.angles.rad((K * x) - (W * t) + phi) ) )
	return Y

while (t < 100):
	while (x < 100):
		Y_Plt = [Wave(x, t)]
		T_Plt = [t]
		X_Plt = [x]
		x += 0.1
	t += 0.1

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(X_Plt, T_Plt, Y_Plt)
plt.show()