start = int(input("Enter the start of range:"))
end = int(input("Enter the end of range:"))

i = start
while(i <= end):
    if(i % 7 == 0 and i % 5 == 0):
        print(i)
    i += 1 