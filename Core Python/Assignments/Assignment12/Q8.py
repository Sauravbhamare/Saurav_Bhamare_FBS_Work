def indexing(str):
    
    return str[::2]
str = input("Enter String:")
result = indexing(str)
print("String after removing characters of odd index",result)