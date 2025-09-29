def even_odd(li):
    li1 = []
    li2 = []
    n = int(input("How many numbers you want to add?"))
    for ele in range(n):
        ele = int(input(f"Enter number{ele+1}:"))
        li.append(ele)
        
    for ele in li:
        if(ele % 2 == 0):
            li1.append(ele)
        else:
            li2.append(ele)
            
            
    print('Even list is',li1)
    print('Odd list is',li2)
li = []
even_odd(li)