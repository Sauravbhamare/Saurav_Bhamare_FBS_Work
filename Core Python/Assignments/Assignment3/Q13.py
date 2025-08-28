units = int(input("Enter the electricity charges:"))

if(units <= 50):
    tot_bill = units * 0.50 + (units * 0.20)
    print(f'total bill: {tot_bill}.')
elif(units <= 100):
    tot_bill = (units * 0.50) + (units * 0.75) + (units * 0.20)
    print(f'total bill: {tot_bill}.')
elif(units <= 250):
    tot_bill = (units * 0.50) + (units * 0.75) + (units * 1.20) + (units * 0.20)
    print(f'total bill: {tot_bill}.')
else:
    tot_bill = (units * 0.50) + (units * 0.75) + (units * 1.20) + (units * 1.50) + (units *0.20)
    print(f'total bill: {tot_bill}.')