def count_char():
    str = input("Enter String:")
    
    countchar = 0
    
    for ele in str:
        if(ele.isalnum()):
            countchar += 1
            
    print("Number of Characters:",countchar)
    
    words = str.split()
    print("Number of words:",len(words))
    
count_char()
            