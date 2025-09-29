def count_lower():
    str = input("Enter String:")
    count = 0
    for ele in str:
        if(ele.islower()):
            count += 1
    print(count)
    
count_lower()
            