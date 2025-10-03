def anagram_strings_list(li):
    angram_group = {}
    group = {}
    for i  in  range(len(li)):
        for j in range(i+1,len(li)):
            if(len(li[i]) == len(li[j])):
                for i , j in zip(li[i],li[j]):
                    if i in angram_group:
                        angram_group[i] = angram_group[i] + 1
                    else:
                        angram_group[i] = 1
                        
                    if j in angram_group:
                        angram_group[j] =angram_group[j] - 1
                    else:
                        angram_group[i] = -1
            
    return angram_group

res = anagram_strings_list()
print(res)
            
        
                        
                        