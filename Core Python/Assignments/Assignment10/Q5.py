def checknum(li):
    
    if(num in li):
        print(f'{num} is in list.')
    else:
        print(f'{num} is not in list.')
            
num = int(input("Enter number to check:"))
li = [10,20,30,40,50]
checknum(li)