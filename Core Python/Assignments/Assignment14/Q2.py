def remove_intersect(s1,s2):
    result = s1 - s1.intersection(s2)
    return result

s1 = {10,20,30,40,60}
s2 = {20,30,60,50,70}

result_set = remove_intersect(s1,s2)

print("Set 1:",s1)
print("Set 2 :",s2)
print("Set 1 after removing set 2:",result_set)