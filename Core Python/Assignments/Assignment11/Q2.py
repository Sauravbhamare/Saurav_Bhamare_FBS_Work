def merge_li():
    li1 = [10,20,30,70]
    li2 = [50,80,20]
    result_li = []
    for ele in li1:
        if(ele not in li2):
            li2.append(ele)
    
    li2.sort()
    print(li2)
    
merge_li()
