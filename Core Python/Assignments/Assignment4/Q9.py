num = int(input("Enter the number:"))
start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))

i = start
while(i <= end):
    if(i % num == 0):
        print(i)
    i += 1