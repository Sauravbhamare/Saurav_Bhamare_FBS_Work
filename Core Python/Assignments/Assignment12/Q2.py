def remove_char(str,n):
    if(n < 0 or n >= len(str)):
        return "Index not found"
    else:
        return str[:n] + str[n+1:]
    
str = 'Firstbit Solutions'
n  = len(str)-1

result = remove_char(str,n)

print("Original String:",str)

print(f"String after removing nth index character:",result)