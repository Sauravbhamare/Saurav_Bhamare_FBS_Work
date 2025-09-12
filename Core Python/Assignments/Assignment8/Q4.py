def oddNo(n):
    sum = 0
    count = 0
    num = 1
    while(count < n):
        sum += num
        num += 2
        count += 1
    print(f'Sum of odd numbers:{sum}')
n = int(input("How many odd numbers addition you want:"))            
oddNo(n)