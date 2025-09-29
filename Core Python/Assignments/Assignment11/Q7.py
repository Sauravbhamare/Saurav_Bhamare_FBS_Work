def intersect_li():
    
    result_li = []
    
    for ele in li1:
        if(ele in li2):
            result_li.append(ele)
    else:
        return result_li

li1 = [1,2,3,4,5,6]
li2 = [2,4,7,8,6]

result = intersect_li()

print("First list:",li1)
print("Second list:",li2)

print("Intersection list:",result)