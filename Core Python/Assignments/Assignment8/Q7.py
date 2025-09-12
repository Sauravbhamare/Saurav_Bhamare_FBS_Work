def sumofDigit():
    num = int(input("Enter number:"))
    sum = 0
    while(num > 0):
        d = num % 10
        num = num // 10
        sum += d
    print(f'Sum of digits of given number:{sum}')
        
sumofDigit()
    