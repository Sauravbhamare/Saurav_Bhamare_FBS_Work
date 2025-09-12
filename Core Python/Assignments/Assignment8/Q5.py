def sumofPrimeNO(num):
    sum = 0
    for i in range(2,num+1):
        for j in range(2,i):
            if(i % j == 0):
                break
        else:
            sum += i
    print(f'Sum of prime number{num}:{sum}.')
            
n = int(input("Enter number:"))
sumofPrimeNO(n)