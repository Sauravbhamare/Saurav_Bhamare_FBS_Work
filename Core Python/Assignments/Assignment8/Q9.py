def calRev(num):
    rev = 0
    while(num > 0):
        digit = num % 10
        rev = rev * 10 + digit
        num = num //10
    return rev

def palindromeNo():
    num = int(input("Enter number:"))
    rev = calRev(num)
    if(rev == num):
        print(f'{num} is a palindrome number.')
    else:
        print(f'{num} is not a palindrome number.')
        
palindromeNo()
