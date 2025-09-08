num = int(input("Enter number:"))
i = 1
fact = 1
sum = 0
while(i<=num):
    fact *= i
    sum += fact
    i += 1
    print(sum)
    
num = int(input("Enter number:"))
i = 1
while(i <= num):
    sum += num ** i
    i += 1
    print(sum)