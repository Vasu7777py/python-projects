import numpy as np
import matplotlib.pyplot as plt

def main():
	Teta0 = 0.01
	g = 120
	L = 100000
	x_plt = []
	y_plt = []
	t = 0
	while (t <= 1000):
		y = (Teta0 * np.cos(np.sqrt(g / L) * t))
		#print(y)
		y_plt.append(y)
		x_plt.append(t)
		t += 0.0001
	for index in range(len(x_plt)):
		print(y_plt[index], x_plt[index]) 

	plt.plot(x_plt, y_plt)
	plt.show()

if __name__ == "__main__":
	main()

