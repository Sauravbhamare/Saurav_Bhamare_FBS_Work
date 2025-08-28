amount = int(input("Enter the Amount:"))

five_hundred = amount // 500
amount = amount % 500

Two_hundred = amount // 200
amount = amount % 200

Hundred = amount // 100
amount = amount % 100

fifty = amount // 50
amount = amount % 50

twenty = amount // 20
amount = amount % 20

ten = amount // 10

print(f'500: {five_hundred} , 200: {Two_hundred} , 100: {Hundred} , 50: {fifty} , 20: {twenty} , 10: {ten}')