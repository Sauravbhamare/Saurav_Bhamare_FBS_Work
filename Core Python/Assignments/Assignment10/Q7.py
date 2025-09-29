def cube_li(li):
    cube_list = []
    n = int(input("How many numbers you want?"))
    for ele in range(n):
        ele = int(input(f"Enter number{ele+1}:"))
        li.append(ele)
    
    for num in li:
        cube = num ** 3
        cube_list.append(cube)
    return cube_list

li = []
result = cube_li(li)
print("Original List:",li)
print("cubed List:",result)



