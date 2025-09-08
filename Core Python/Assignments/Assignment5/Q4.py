num = int(input("Enter the number:"))
temp = num
sum = 0
count=0
while(temp > 0):
    count += 1
    temp = temp // 10
temp = num
while(temp > 0):
    d = temp % 10
    sum += d ** count
    temp = temp // 10
    
if(sum == num):
    print(f'{num} is a armstrong number.')
else:
    print(f'{num} is not a armstrong number.')
    