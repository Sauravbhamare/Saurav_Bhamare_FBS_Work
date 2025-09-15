def fibo(n ,a ,b):
    if(n>0):
        c = a + b
        print(c ,end= ' ')
        fibo(n-1,b,c)
        
num = int(input("How many numbers you want:"))
fibo(num,-1,1)
    