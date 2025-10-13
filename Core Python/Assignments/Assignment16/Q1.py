class Book:
    count = 0
    def __init__(self,id=0,name='',price=0,author=''):
        self.bid = id
        self.bname = name
        self.price = price
        self.author = author
        Book.count += 1
        
    def Showbook(self):
        print("Book ID:",self.bid)
        print("Book Name:",self.bname)
        print("Price:",self.price)
        print("Author:",self.author)
        
    def __del__(self):
        Book.count -= 1
        print("Program executed successfully.")
        
    @staticmethod
    def showcount():
        print("Count of books:",Book.count)
    
        
b1 = Book(121,'Math',1200,'saurav')
b1.Showbook()

b2 = Book()
b2.Showbook()

Book.showcount()