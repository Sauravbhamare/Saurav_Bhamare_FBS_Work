def calRev(num):
    rev = 0
    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print(f'Reverse of number:{rev}')
    
n = int(input("Enter number:"))

calRev(n)