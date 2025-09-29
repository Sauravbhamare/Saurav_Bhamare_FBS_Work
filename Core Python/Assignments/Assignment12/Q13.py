def count_digit():
    str = input("Enter String:")
    countdigit = 0
    countletter = 0
    
    for ele in str:
        if(ele.isdigit()):
            countdigit += 1
        elif(ele.isalpha()):
            countletter += 1
            
    print("Digits in string:",countdigit)
    print("Letters in string:",countletter)
    
count_digit()
            