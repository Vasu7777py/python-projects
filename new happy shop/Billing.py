from dataclasses import dataclass

import stock
import Costumers
import Labours

Stock_list_link = stock.Stock
Stock_info = stock.Stock
Costumer = Costumers.Costumer
Labour = Labours.Labour

@dataclass
class Billing:
    Bill_id: str
    billing_Costumer: Costumers.Costumer
    billing_Costumer_name: str
    billing_Costumer_phone: str
    billing_products: list
    product_count: int
    bill_amount: float
    billing_labour: Labours.Labour
    
    #bill_tax: float
    #bill_net_amount: float

    def __init__(self ,Bill_code ,Costumer ,Labour):
        self.Bill_id = Bill_code
        self.billing_Costumer = Costumer
        self.billing_Costumer_name = (self.billing_Costumer.Costumer_firstname + "." + self.billing_Costumer.Costumer_lastname)
        self.billing_Costumer_phone = (self.billing_Costumer.Costumer_phonenumber)
        self.bill_amount = 0.0
        self.billing_products = []
        self.product_count = 0
        self.billing_labour = Labour

    def generate_bill_line(self ,Stock_info,Quantity):
        # GENERATING a line or CREATING a line in a bill
        temp_check = Stock_info.Stock_check()
        if Stock_info != None:
            if temp_check < Quantity:
                # checking if entered QUANTITY is avaliable or not
                print("LOW ON STOCK!!!...")
                print("Avaliable stock..." + str(temp_check))
                return False , None
            else:
                self.product_count += 1
                # CREATING a dict and appending it to a list 
                # to creating a efficient way of storing data
                self.billing_products.append({
                    "Product_code" : Stock_info.Stock_id ,
                    "product_name" : Stock_info.Stock_name ,
                    "Quantity" : Quantity ,
                    "rate" : Stock_info.Stock_sellingprise ,
                    "discount" : Stock_info.Stock_discount ,
                    "amount" : self.discount_amount(Stock_info ,Quantity)
                    })
                Stock_info.stock_update(Quantity)
                return True ,self.billing_products[-1].amount
        else:
            return False , None
    
    def discount_amount(self ,Stock_info ,Quantity):
        if Stock_info.Stock_discount == None:
            # Calculating Amount for a perticular stock of quantity
            return(float(Quantity * Stock_info.Stock_sellingprise))
        else:
            # Calculating Amount for a perticular stock of quantity and discount
            return(float( Quantity * Stock_info.Stock_sellingprise * (1 - (Stock_info.Stock_discount / 100 ))))
    
    def generate_bill(self ,Stock_list_link):
        flag = True
        while flag != False:
            is_gen ,Amount = self.generate_bill_line(stock.stock_search(Stock_list_link ,input("Enter product code: ")) ,int(input("Enter the quantity : ")))
            if is_gen == False:
                print("Error!!!... \nWas not able to add the proudct to the bil...")
            else:
                self.bill_amount = self.bill_amount + Amount
                check = input("Do u want to continue yes(1)/no(0) : ")
                if check == "0":
                    flag = False
    
    def print_bill(self):
        for i in range(len(self.billing_products)):
            print("Product code : " + self.billing_products[i].prouduct_code)
            print("Product name : " + self.billing_products[i].product_name)
            print("Quantity : " + str(self.billing_products[i].Quantity))
            print("Rate : " + str(self.billing_products[i].rate))
            print("Discount : " + str(self.billing_products[i].discount) + "%")
            print("Amount : "+ str(self.billing_products[i].amount))
        print("Net Amount : " + str(self.bill_amount))
