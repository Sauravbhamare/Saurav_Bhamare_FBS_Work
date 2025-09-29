def even_odd_li():
    even_li = []
    odd_li = []
    
    for num in li:
        if(num % 2 == 0):
            even_li.append(num)
        else:
            odd_li.append(num)
    
    print("Original ist:",li)
    print("Even list:",even_li)
    print("Odd list:",odd_li)

li = [1,2,3,4,5,6,7,8,9]
even_odd_li()

    

    

