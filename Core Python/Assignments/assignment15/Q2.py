class Product:
    
    def __init__(self,pid=0,pname='',price=0,quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
        
    def showData(self):
        print(f'Product_ID:{self.pid}\nProduct_Name:{self.pname}\nPrice:{self.price}\nQuantity:{self.quantity}')
        
        
    def __del__(self):
        print("Destructor is called.")
        
    def showdiscount(self,price):
        discount = price*10/100
        print("Discount",discount)
        
p1 = Product(11,'Laptop',47800,1)
p2 = Product()
p1.showData()
print('***************************')
p2.showData()