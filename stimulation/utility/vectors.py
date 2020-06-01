import Math

Vector = Math.Vector

class Force:
	def __init__(self, magnitude_list):
		self.Vector = Vector(magnitude_list)

class NaturalVectors:
	def __init__(self, magnitude_list, unit):
		self.Vector = Vector(magnitude_list)
		self.Unit = unit

class Accleration(NaturalVectors):
	def __init__(self, Type, magnitude_list, unit):
		self.Type = Type
		NaturalVectors.__init__(self, magnitude_list, unit)

class Weight(Force):
	def __init__(self, mass, unit, accle : Accleration):
		if (unit == "Kg"):
			Magnitude = (mass * accle.Vector.Magnitude)
			self.Force = Force.__init__(self, Magnitude)
		elif (unit == "g"):
			Magnitude = ((mass / 1000) * accle.Vector.Magnitude)
			self.Force = Force.__init__(self, Magnitude)
		else:
			print("Error!!!")
			exit()
		self.Unit = "N"

class PredefinedVectors:
	@staticmethod
	def AccDueToGravity():
		self = Accleration("Linear", [0, -9.80665, 0], "ms-2")
		return self

