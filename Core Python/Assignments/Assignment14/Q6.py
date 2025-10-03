def max_product_pair(li):
    s1 = list(set(li))
    max_product = 0
    pair = ()
    
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            product = li[i] * li[j]
            if(product > max_product):
                max_product = product
                pair = (li[i] , li[j])
                
    return pair , max_product

li = [2,3,4,6,7,2]
result , product = max_product_pair(li)

print("Pair with max product:",result)

print("Maximum product:",product)