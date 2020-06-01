import matplotlib.pyplot as plt

class animal:
	def __init__(self, Sex:str, Life_cycle_period:int, Muration_age:int):
		self.Life_cycle_period = Life_cycle_period
		self.Muration_age = Muration_age
		self.Sex = Sex

class Cow(animal):
	def __init__(self, Sex:str, Life_cycle_period:int, Muration_age:int):
		animal.__init__(self, Sex, Life_cycle_period, Muration_age)
		self.Age = 0
		self.Latest_birth_sex = None

	def Age_increment(self):
		self.Age += 1

	def Is_Muratured(self):
		if (self.Age >= self.Muration_age):
			return True
		else:
			return False

	def Reproduction(self):
		if (self.Is_Muratured() and (self.Sex == "Female")):
			if ((self.Latest_birth_sex == None) or (self.Latest_birth_sex == "Male")):
				self.Latest_birth_sex = "Female"
				return "Female"
			else:
				self.Latest_birth_sex = "Male"
				return "Male"
		else:
			return None

	def Is_dead(self):
		if (self.Age <= self.Life_cycle_period):
			return False
		else:
			return True

def main():
	run_years = 120
	life_present = []

	x_plt = []
	sex_Female = []
	sex_male = []
	life = []

	life_present.append(Cow("Female", 30, 15))
	for years in range(run_years):
		birth = []
		kill = []
		Life_count = 0
		Female_count = 0
		Male_count = 0
		for cow in life_present:
			if not cow.Is_dead():
				Life_count += 1
				if (cow.Sex == "Female"):
					Female_count += 1
				else:
					Male_count += 1

				cow.Age_increment()
				if cow.Is_Muratured():
					baby_cow = cow.Reproduction()
					if (baby_cow != None):
						birth.append(Cow(baby_cow, cow.Life_cycle_period, cow.Muration_age))
			else:
				kill.append(cow)
		for cow in birth:
			life_present.append(cow)
		for cow in kill:
			life_present.remove(cow)

		print(years, len(life_present), Female_count)

		x_plt.append(years)
		sex_Female.append(Female_count)
		sex_male.append(Male_count)
		life.append(Life_count)

	plt.plot(x_plt, life, color = "#33FF33", label = "Total")
	plt.plot(x_plt, sex_Female, color = "#CC00CC", label = "Female")
	plt.plot(x_plt, sex_male, color = "#000000", label = "Male")
	plt.legend()
	plt.show()

if __name__ == '__main__':
	main()