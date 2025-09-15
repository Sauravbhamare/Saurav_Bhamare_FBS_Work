def sum_digit(n):
    if(n==0):
        return 0
    else:
        digit = n % 10
        return digit + sum_digit(n//10)
    

num = int(input("Enter number:"))
print("Sum of digits:",sum_digit(num))