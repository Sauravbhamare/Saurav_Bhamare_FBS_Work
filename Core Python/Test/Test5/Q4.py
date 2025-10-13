def occurence_di(li):
    frequency = {}
    
    for num in li:
        if(num in frequency):
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    print(frequency)
    
li = [1,3,4,1,2,3,6,7,1,2,4]
occurence_di(li)

