def remove_key(dict):
    key = int(input("Enter key to remove:"))
    dict.pop(key)
    print(dict)
dict = {1:'Saurav',2:'Sahil',3:'Ankit'}
remove_key(dict)

