def three_li():
    li1 = []
    li2 = []
    li3 = []
    n = int(input("How many numbers you want to add?"))
    for num in range(n):
        num = int(input(f"Enter number{num+1}:"))
        li1.append(num)
        li2.append(num ** 2)
        li3.append(num ** 3)
        
    print(li1)
    print(li2)
    print(li3)
    
    
three_li()