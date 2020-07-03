
#import numpy as np

class Linear:
	def __init__(self, m = 1.0, c = 0.0):
		self.m = m
		self.c = c

	def __reper__(self):
		return f"m : {self.m}, c : {self.c}"

	def get_slope(self):
		return self.m

	def get_coffecient(self):
		return self.c

	def copy(self):
		return Linear(self.m, self.c)

	def solve(self, x):
		return ((self.m * x) + self.c)

class Linear_Regression:
	def __init__(self, learning_rate = 0.001):
		self.equation = Linear()
		self.learning_rate = learning_rate
		self.Greadent_Factor = None

		self.Number_trials = 0
		self.States = []

		self.State_run = False

	def Creat_Model(self, input_list, output_list):
		self.State_run = True
		while self.State_run:
			current_cost = Linear_Regression.CostFunction(input_list, output_list, self.equation)
			self.Number_trials += 1
			self.States.append((self.equation.m, self.equation.c, current_cost))
			self.Greadent_Deasend()
			print(f"cost : {current_cost}, equation : {self.equation.__reper__()}, trys : {self.Number_trials}")

		print(self.equation)

	def Greadent_Deasend(self):
		if (len(self.States) <= 1):
			m = self.equation.m - self.learning_rate
			c= self.equation.c - self.learning_rate
		else:
			m1, c1, prev_cost = self.States[-2]
			m2, c2, cur_cost = self.States[-1]
			div_m = ((m2 - m1) / self.learning_rate)
			div_c = ((c2 - c1) / self.learning_rate)
			if (abs(cur_cost) <= 0.001):
				self.State_run = False
				return
			else:
				m = (self.equation.m - (div_m * self.learning_rate))
				c = (self.equation.c - (div_c * self.learning_rate))

		self.equation = Linear(m, c)

	@classmethod
	def CostFunction(cls, input_list, output_list, equation:Linear):
		cost = 0
		for Index in range(len(input_list)):
			cost += pow((equation.solve(input_list[Index]) - output_list[Index]), 2)
		
		return ((1/2)*(cost))

def main():
	y = [6.6, 8.8, 5.4, -1.8, 0, -4]
	x = [3.926, 4.741, 3.481, 0.815, 1.481, 0]
	model = Linear_Regression()
	model.Creat_Model(x, y)

if (__name__ == "__main__"):
	main()
