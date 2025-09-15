def cnt(num):
    if(num == 0):
        return 0
    else:
        return 1 + cnt(num//10)
    
def power(num,count):
    if(num==0):
        return 0
    else:
        digit = num % 10
        return (digit ** count) + power(num//10,count)
    
def is_armstrong(num):
    digits = cnt(num)
    result = power(num,digits)
    if(num == result):
        print(f'{num} is a armstrong number.')
    else:
        print(f'{num} is not armstrong number.')
        
num = int(input("Enter number:"))
is_armstrong(num)