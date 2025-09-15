def primeNum(n,i=2):
    if(n<=1):
        return 0
    if(i * i > n):
        return 1
    if(n % i == 0):
        return 0
    return primeNum(n,i+1)

num = int(input("Enter number:"))
result = primeNum(num)
if(result == 1):
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')