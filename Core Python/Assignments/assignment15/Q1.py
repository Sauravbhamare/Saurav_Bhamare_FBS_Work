class Book:
    
    def __init__(self,bid=0,bname='',price=0,author=''):
        self.bid = bid
        self.bookname = bname
        self.price = price
        self.author = author
    
    def __del__(self):
        print("Destructor called.")
        
        
    def showData(self):
        print(f'BOOK_ID:{self.bid}\nBOOK_NAME:{self.bookname}\nPRICE:{self.price}\nAUTHOR:{self.author}')
        
        
    

b1 = Book(121,'MATHEMATICS',1200,'sahil')
b2 = Book()

b1.showData()
print("**************************************")
b2.showData()