def sum_pair(li, target_sum):
    pairs = []
    
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            if(li[i]+li[j] == target_sum):
                pairs.append((li[i] , li[j]))
                
    return pairs

li = [1,2,3,4,5,6,7]
target = int(input("Enter target sum:"))

res = sum_pair(li,target)

print(f"Pairs with sum {target}:")
for pair in res:
    print(pair)