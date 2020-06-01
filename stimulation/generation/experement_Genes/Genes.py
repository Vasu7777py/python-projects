
"""
KeyError : when given key is not present in the dict
"""

class Genes:
	def __init__(self, _name:str, _size:int, _type:str, _power:float, _per_transfer:float, _active:bool):
		self._name = _name
		self._size = _size
		self._type = _type
		self._power = _power
		self._per_transfer = _per_transfer
		self._active = _active

	def print_gene_info(self):
		print(f"name : {self._name}")
		print(f"size : {self._size}")
		print(f"type : {self._type}")
		print(f"power : {self._power}")
		print(f"per_transfer : {self._per_transfer}")
		print(f"active : {self._active}")

	def get_gene_info(self):
		gene = {
			"name" : self._name,
			"size" : self._size,
			"type" : self._type,
			"power" : self._power,
			"per_transfer" : self._per_transfer,
			"active" : self._active
		}
		return gene

class Natural_Genes:
	class Surival:
		@staticmethod
		def High_Reproductivity(name:str):
			if (name == "HR1"):
				gene = Genes("HR1", 7, "Surival_Reproductivity", 7.8, 27.3, True)
			elif (name == "HR2"):
				gene = Genes("HR2", 7, "Surival_Reproductivity", 9.7, 24.1, True)
			elif (name == "HR3"):
				gene = Genes("HR3", 7, "Surival_Reproductivity", 35.2, 1.2, True)
			return gene

