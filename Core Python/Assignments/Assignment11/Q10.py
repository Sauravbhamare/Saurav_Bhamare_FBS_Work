def remove_even_li():
    li = []
    n = int(input("How many numbers you want to add?"))
    for num in range(n):
        num = int(input(f"Enter number{num+1}:"))
        if(num % 2 != 0):
            li.append(num)
    return li
    
    
result = remove_even_li()
print("List after removing even numbers",result)
        
        
