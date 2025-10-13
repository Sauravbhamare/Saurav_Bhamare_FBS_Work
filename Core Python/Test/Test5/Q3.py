def sort_subli(li):
    sorted_li = sorted(li , key = lambda x:x[2])
    print(sorted_li)
    
data = [[101,'Seema',45000],[340,'Rajani',13000],[210,'Tannu',14000],[320,'Suresh',35000]]
sort_subli(data)