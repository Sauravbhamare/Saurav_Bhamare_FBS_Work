num = int(input("Enter the Days:"))

Y = num // 365
X = num % 365

W = X // 7
Z = X % 7

D = Z % 7

print(f'Years: {Y}, Weeks: {W}, Days: {D}. ') 