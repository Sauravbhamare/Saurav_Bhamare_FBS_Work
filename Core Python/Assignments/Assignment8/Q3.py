def sumofSeries():
    num = int(input("Enter number:"))
    sum_num = 0
    for i in range(num+1):
        sum_num += i
    print(f'Sum of numbers series:{sum_num}.')
        
    fact = 1
    sum_fact = 0
    for i in range(1,num+1):
        fact *= i
        sum_fact += fact
    print(f'Sum of factorial series:{sum_fact}.')
        
    sum_raise = 0
    for i in range(num+1):
        sum_raise += i ** i
    print(f'Sum of series:{sum_raise}')
    
sumofSeries()