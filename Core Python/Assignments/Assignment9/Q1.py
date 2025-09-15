def fact_num(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact_num(n-1)
    
def sum_fact(n):
    if(n==0):
        return 0
    else:
        return fact_num(n) + sum_fact(n-1)

n = int(input("How many factorial you want"))
print(f'Sum of factorials:{sum_fact(n)}')