def isspace():
    str1 = input("Enter String:")
    li = [char for char in str1 if char == ' ']
    print(li)
    print(len(li))
isspace()