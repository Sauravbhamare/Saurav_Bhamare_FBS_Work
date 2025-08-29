p1 = int(input("Enter the price for product 1:"))
p2 = int(input("Enter the price for product 2:"))
p3 = int(input("Enter the price for product 3:"))
p4 = int(input("Enter the price for product 4:"))
p5 = int(input("Enter the price for product 5:"))

sum = p1 + p2 + p3 + p4 + p5
gst = sum * 0.18

total_bill = sum + gst
print(f'total bill of shopping including 18% GST:{total_bill}')