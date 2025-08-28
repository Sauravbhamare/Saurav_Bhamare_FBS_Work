cost = int(input("Enter the cost price of book:"))
discount = int(input("Enter the discount of book:"))

selling_price = cost * (1 - (discount / 100))
print(f'Selling price of book is {selling_price}')