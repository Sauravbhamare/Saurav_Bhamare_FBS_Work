def union_li(li1,li2):
    result_li = []
    
    for ele in li1:
        if(ele in li2):
            result_li.append(ele)
            
    print(result_li)
    
li1 = [1,2,3,4,5,6]
li2 = [2,4,6,8]
union_li(li1,li2)
    