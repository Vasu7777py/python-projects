from os import system
from time import sleep
import pandas as pd
stockdata = []
class Stock:
	def __init__(self, Stock_Code:str, Stock_Name:str, Stock_Quantity:int, Cost_prize:float, Selling_prize:float, Stock_Soled:int, Stock_Profit:float):
		self.Stock_Code = Stock_Code
		self.Stock_Name = Stock_Name
		self.Stock_Quantity = Stock_Quantity
		self.Cost_prize = Cost_prize
		self.Selling_prize = Selling_prize
		self.Stock_Soled = Stock_Soled
		self.Stock_Profit = Stock_Profit

	def get_stock_data(self):
		print(f"Stock_Code : {self.Stock_Code}")
		print(f"Stock_Name : {self.Stock_Name}")
		print(f"Stock_Quantity : {self.Stock_Quantity}")
		print(f"Cost_prize : {self.Cost_prize}")
		print(f"Selling_prize : {self.Selling_prize}")
		print(f"Stock_Soled : {self.Stock_Soled}")
		print(f"Stock_Profit : {self.Stock_Profit}")

	def sell_Stock(self):
		pass
		
	@staticmethod
	def generate_Stock():
		Stock_Data = pd.read_csv("data/stockdata.csv")
		Sdata = Stock_Data.iloc[:, [0, 1, 2, 3, 4]].values
		for data in Sdata:
			Stock_Code = data[0]
			Stock_Name = data[1]
			Stock_Quantity = data[2]
			Cost_prize = data[3]
			Selling_prize = data[4]
			Stock_Soled = None
			Stock_Profit = None
			stock = Stock(Stock_Code, Stock_Name, Stock_Quantity, Cost_prize, Selling_prize, Stock_Soled, Stock_Profit)
			stockdata.append(stock)

Stock.generate_Stock()
for data in stockdata:
	print("\n")
	data.get_stock_data()
