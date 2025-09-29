def is_li():
    li = []
    res = 0
    n = int(input("How many elements you want to add?"))
    for ele in range(n):
        ele = int(input(f"Enter element{ele+1}:"))
        li.append(ele)
        res += ele
    return res
result = is_li()
print("Sum of list:",result)