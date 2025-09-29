def three_list():
    li1 = []
    li2 = []
    li3 = []

    n = int(input("How many numbers do you want to add? "))
    
    for i in range(n):
        ele = int(input(f"Enter element {i + 1}: "))
        li1.append(ele)

    for ele in li1:
        li2.append(ele ** 2)

    for ele in li1:
        li3.append(ele ** 3)

    print("Original list:", li1)
    print("Squared list:", li2)
    print("Cubed list:", li3)

three_list()
