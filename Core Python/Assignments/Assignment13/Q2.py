def concatenate_dict(d1,d2):
    
    result = d1.copy()
    result.update(d2)
    
    print(result)
dict1 = {1:'Saurav',2:'Sahil',3:'Ankit'}
dict2 = {4:'Mayur',5:'Shubham',6:'Sunil'}
concatenate_dict(dict1,dict2)
