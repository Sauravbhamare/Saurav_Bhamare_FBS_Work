n = int(input("Enter the number:"))
fact = 1
sum = 0
for i in range(1,n+1):
    fact *= i
    sum += i/fact
print(f'Sum of series:{sum}.')
    
    