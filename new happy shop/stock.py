from dataclasses import dataclass

@dataclass
class Stock:
    Stock_id: str
    Stock_name: str
    Stock_description: str
    Stock: int
    Stock_source: str
    stock_is_avaliable: bool
    Stock_costprise: float
    Stock_sellingprise: float
    Stock_discount: float

    def __init__(self ,sid ,name ,stock ,descripation ,avaliable ,sellingprise ,costprise ,discount ,source):
        self.Stock_id = sid
        self.Stock_name = name
        self.Stock_description = descripation
        self.Stock = stock
        self.stock_is_avaliable = avaliable
        self.Stock_sellingprise = sellingprise
        self.Stock_costprise = costprise
        self.Stock_discount = discount
        self.Stock_source = source

    def stock_detiles(self):
        print("Name : " + self.Stock_name)
        print("id : " + self.Stock_id)
        print("Prize : " + str(self.Stock_sellingprise))
        print("DISCOUNT : " + str(self.Stock_discount) + "% OFF")
        print("Stock avaliable : " + str(self.Stock))
    
    def stock_update(self ,stock_Quantity):
        if stock_Quantity > self.Stock:
            print("STOCK ERROR!!!!!....")
        else:
            self.Stock = self.Stock + stock_Quantity
            if self.Stock == 0:
                self.stock_is_avaliable = False
    
    def Stock_check(self):
        return self.Stock

    def Stock_info(self):
        self.stock_detiles()
        print("is avaliable : " + str(self.stock_is_avaliable))
        print("Stock source : " + self.Stock_source)
        print("Stock descripation : " + self.Stock_description)

Stock_list_link = Stock

def stock_search(Stock_list_link ,Stock_id):
    for i in range(len(Stock_list_link)):
        if Stock_id == Stock_list_link[i].Stock_id:
            return(Stock_list_link[i])
        else: 
            return None
