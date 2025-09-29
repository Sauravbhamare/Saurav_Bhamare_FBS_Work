def odd_num(li):
    odd_list = []
    for ele in li:
        if(ele % 2 != 0):
            odd_list.append(ele)
    return odd_list


        
li = [1,2,3,4,5,6]
odd_list = odd_num(li)

print("Original ist:",li)
print("List After removing even numbers:",odd_list)