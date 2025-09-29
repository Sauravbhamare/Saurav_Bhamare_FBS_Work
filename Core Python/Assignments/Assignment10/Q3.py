def sec_max():
    max_num = 0
    smax_num = 0
    li = []
    n = int(input("How many numbers you want?"))
    
    for ele in range(n):
        ele = int(input(f"Enter element{ele+1}:"))
        li.append(ele)
        
    
    for ele in li:
        if(ele > max_num):
            smax_num = max_num
            max_num = ele
        elif(ele > smax_num and ele != max_num ):
            smax_num = ele
    print("Second Maximum number is",smax_num)



sec_max()