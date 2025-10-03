def different_ele(s1,s2):
    
    return(s1.difference(s2))
    
s1 = {10,20,30,40}
s2 = {20,50,60,10}
Result_set = different_ele(s1,s2)
print("Set 1:",s1)
print("Set 2:",s2)
print("Result set:",Result_set)