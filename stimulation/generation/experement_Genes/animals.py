import Genes
from Genes import Natural_Genes as NG

class animals:
	def __init__(self, genes:list, _name:str, _sex:str, _type:str, _per_transfer:float, _maruturation_time:int, _gestation_period:int):
		self.genes = genes
		self._name = _name
		self._sex = _sex
		self._type = _type
		self._per_transfer = _per_transfer
		self._maruturation_time = _maruturation_time
		self._gestation_period = _gestation_period

genes = [NG.Surival.High_Reproductivity("HR3"), NG.Surival.High_Reproductivity("HR2")]
Animals = animals(genes, "gueric", "Female", "reptile", 50.4, 25, 10)
print(Animals.genes[0].print_gene_info(), "\n")
print(Animals.genes[1].print_gene_info())
