def sum_three_num(li,target_sum):
    pair = set()
    
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            for k in range(j+1,len(li)):
                if(li[i] + li[j] + li[k] == target_sum):
                    sum_pair = (li[i] , li[j] ,li[k])
                    pair.add(sum_pair)
                    
    return pair

li = [1,2,3,4,5,6,7,8]
target = int(input("Enter target sum:"))
res = sum_three_num(li,target)
print(res)