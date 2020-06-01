from dataclasses import dataclass
import stock

@dataclass
class StockManager:
    stockMap: dict

    def __init__(self):
        self.stockMap = {}

    def addStock(self, stockObj: stock.Stock):
        self.stockMap.append({stockObj.Stock_id : stockObj})

    def print__(self):
        for sk in self.stockMap.keys:
            print(sk)
            self.stockMap.values(sk).stock_detiles()
s = dict
st = stock.Stock("123", "Test 1", "For test 1", 23, "Self", True, 12.3, 13.5, 0)
s.update({st.Stock_id : st})
st = stock.Stock("124", "Test 2", "For test 2", 24, "Self 1", True, 12.5, 13.6, 0)
s.update({st.Stock_id : st})
for sk in s.keys:
    print("key = " + sk)
    st = s.get(sk)
    st.stock_detiles