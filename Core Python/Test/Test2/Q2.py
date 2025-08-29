num = int(input("Enter three digit number:"))

d1 = num % 10
num = num // 10

d2 = num % 10
num = num // 10

d3 = num % 10

if(d2 == (d3*2) and d1 == (d3/2)):
    print("Yes,you have done it.")
else:
    print("Please try next time.")