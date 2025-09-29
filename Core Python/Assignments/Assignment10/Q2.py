def minMax():
    li = []
    n = int(input("How many numbers you want?"))
    
    for ele in range(n):
        ele = int(input(f"Enter number{ele+1}:"))
        li.append(ele)
        
    min_num = li[0]
    max_num = li[0]
    
    for ele in li:
        if(ele > max_num):
            max_num = ele
        if(ele < min_num):
            min_num = ele
            
    print(f'Minimum element in list is {min_num}')
    print(f'Maximum element in list is {max_num}')
    
    
minMax()