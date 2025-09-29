def sum_dict(d):
    sum = 0
    for value in d.values():
        sum += value
    print(f'Sum of dictionary:{sum}')
    
d = {1:12,2:12}
sum_dict(d)