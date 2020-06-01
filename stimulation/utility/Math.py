import numpy as np

class Constants:
	PIE = (22/7)

class angles:
    @staticmethod
    def rad(angle_deg:float):
        angle_r = ((angle_deg * Constants.PIE)/180)
        return angle_r

    @staticmethod
    def deg(angle_rad:float):
        angle_deg = ((angle_rad * 180)/Constants.PIE)
        return angle_deg

class Vector:
	def __init__(self, Magnitude_list):
		self.Magnitude = np.array(Magnitude_list)
		self.UpdateDirection()
		self.Cosines = self.DirectionalCosines()
		self.Angles = self.VectorAngles()			# is in radians

	def UpdateDirection(self):
		D_list = ["x", "y", "z"]
		for index in range(3):
			if (self.Magnitude[index] == 0):
				D_list[index] = ""
			elif (self.Magnitude[index] < 0):
				D_list[index] = "-" + D_list[index]
			self.Direction = tuple(D_list)

	@staticmethod
	def DotProduct(self, other):
		x1, y1, z1 = tuple(self.Magnitude)
		x2, y2, z2 = tuple(other.Magnitude)
		Prod = ((x1 * x2) + (y1 * y2) + (z1 + z2))
		return Prod

	@staticmethod
	def CrossProduct(self, other):
		x1, y1, z1 = tuple(self.Magnitude)
		x2, y2, z2 = tuple(other.Magnitude)
		Prod = []
		Prod.append((y1 * z2) - (z1 * y2))
		Prod.append((z1 * x2) - (x1 * z2))
		Prod.append((x1 * y2) - (y1 * x2))
		return Vector(Prod)

	def DirectionalCosines(self):
		a, b, c = tuple(self.Magnitude)
		Base = np.sqrt((a*a) + (b*b) + (c*c))
		CosAlpha = (a / Base)
		CosBeta = (b / Base)
		CosGamma = (c / Base)
		return (CosAlpha, CosBeta, CosGamma)

	def VectorAngles(self):
		CosAlpha, CosBeta, CosGamma = self.Cosines
		Alpha = np.arccos(CosAlpha)
		Beta = np.arccos(CosBeta)
		Gamma = np.arccos(CosGamma)
		return (Alpha, Beta, Gamma)
