def rev_num():
    li = []
    n = int(input("How many numbers you want?"))
    for ele in range(n):
        ele = int(input(f"Enter number{ele+1}:"))
        li.append(ele)
    
    
    print("Reversed list:",li[::-1])
    
rev_num()
