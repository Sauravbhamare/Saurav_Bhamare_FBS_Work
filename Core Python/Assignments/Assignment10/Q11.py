def div_mn(li):
    m = 2
    n = 3
    for ele in li:
        if(ele % m == 0 and ele % n == 0):
            print(ele)
            
li = [6,12,5,7]

div_mn(li)