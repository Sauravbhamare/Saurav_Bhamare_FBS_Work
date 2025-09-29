str1 = 'abccd'
str2 = 'abcdc'

if(len(str1) == len(str2)):
    di = {}
    for i , j in zip(str1,str2):  #zip is used for two objects in one object
        if i in di:
            di[i] = di[i] + 1
        else:
            di[i] = 1
            
            
        if j in di:
            di[j] = di[j] - 1
        else:
            di[j] = -1
            
    print(di)
    
    for val in di.values():
        if(val != 0):
            print("Strings are not Anagram.")
            break
    else:
        print("Strings are Anagram.")
        
else:
    print("Strings are not Anagram.")
        