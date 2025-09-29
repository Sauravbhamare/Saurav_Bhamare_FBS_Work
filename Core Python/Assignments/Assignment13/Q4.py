def square_dict(n):
    
    result = {}
    for x in range(1,n + 1):
        result[x] =  x * x
    return result

n = int(input("How many numbers you want:"))
result = square_dict(n)
print("Squared Dictionary:",result)