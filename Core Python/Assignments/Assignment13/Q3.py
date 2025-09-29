def key_check(d1,key):
    
    if(key in d1):
        print(f'{key} exists in Dictionary.')
    else:
        print(f'{key} not exist in dictionary.')
        
dict = {1:'Saurav',2:'Sahil',3:'Ankit'}
key = int(input("Enter key to check:"))

key_check(dict,key)