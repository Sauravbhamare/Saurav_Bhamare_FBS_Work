def sec_ele(li):
    return li[1]

li = [[1,2],[4,3],[2,2],[8,1]]


sorted_li = sorted(li,key=sec_ele)

print("Sorted list:",sorted_li)