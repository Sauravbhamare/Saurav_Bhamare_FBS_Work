num = int(input("Enter the number:"))
sum = 0
temp = num
while(temp > 0):
    d = temp % 10
    fact = 1
    for i in range(1,d+1):
        fact =fact * i
    sum = sum + fact 
    temp = temp // 10

if(sum == num):
    print(f'{num} is a strong number.')
else:
    print(f'{num} is not a strong number.')
