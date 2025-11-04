def palindrome(limit):
    n =0
    while(n<=limit):
        if(str(n) == str(n)[::-1]):
            yield n
        n += 1
    return n
limit = int(input("Enter limit:"))
gen = palindrome(limit)
for num in gen:
    print(num)    
