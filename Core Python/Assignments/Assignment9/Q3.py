def rev_num(n ,rev=0):
    if(n == 0):
        return rev
    else:
        digit = n % 10
        rev = rev * 10 + digit
        return rev_num(n // 10, rev)
num = int(input("Enter number:"))
print("Reversed number:", rev_num(num))