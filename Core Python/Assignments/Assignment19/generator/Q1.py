# def fibo_gen(limit):
#     a , b = 0 , 1
    
#     while a <= limit:
#         yield a
#         a , b = b , a + b
    
# limit = int(input("Enter limit:"))        
# for num in fibo_gen(limit+1):
#     print(num)
    
    
def fibonum(limit):
    a , b = 0 , 1
    
    while a<=limit:
        yield a
        a , b = b , a+b
        
limit = int(input("Enter limit:"))
for num in fibonum(limit+1):
    print(num)