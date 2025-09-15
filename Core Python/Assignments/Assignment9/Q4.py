def sum_of_series(n):
    if(n == 0):
        return 0
    else:
        return n + sum_of_series(n-1)
num = int(input("How many numbers addition you want:"))
print("Sum of series:",sum_of_series(num))