def mult_dict(d):
    multiply = 1
    for value in d.values():
        multiply *= value
    print(f"Multiplication of Dictionary:{multiply}")
    
d = {1:2,2:12,3:24}
mult_dict(d)