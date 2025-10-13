class Shirt:
    price = 1000
    def __init__(self,sid=0,sname='',type='',price=0,size=''):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size
        
        
    def __del__(self):
        print("Destructor is called.")
        
    def displayData(self):
        print("Shirt Id",self.sid)
        print("Shirt name:",self.sname)
        print("Shirt type:",self.type)
        print("Shirt price:",self.price)
        print("Shirt Size:",self.size)
        
    @classmethod
    def increasePriceBy10(cls):
        cls.price += cls.price * 10 / 100

    @classmethod
    def decreasePriceBy10(cls):
        cls.price -= cls.price * 10 / 100
        
s1 = Shirt(11,'Cotton','Formal',500,'M')
s1.displayData()
print("************************************")
s2 = Shirt()
s2.displayData()
