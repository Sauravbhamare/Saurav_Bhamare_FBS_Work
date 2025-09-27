def factor_num(n):
    for i in range(1,n+1):
        if(n % i == 0):
            print(i)
n = int(input("Enter number:"))
factor_num(n)