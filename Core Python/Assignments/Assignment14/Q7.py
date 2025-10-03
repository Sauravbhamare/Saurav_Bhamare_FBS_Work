def missing_ele(s1,s2):
    new_s1 = s1.difference(s2)
    new_s2 = s2.difference(s1)
    


    print("Elements missing in set2:",new_s1)
    print("Elements missing in set1:",new_s2)
s1 = {10,20,30,40,50}
s2 = {30,60,40,90}

missing_ele(s1,s2)