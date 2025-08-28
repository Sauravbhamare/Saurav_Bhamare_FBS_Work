Angle1 = int(input("Enter the first angle:"))
Angle2 = int(input("Enter the second angle:"))
Angle3 = int(input("Enter the third angle:"))

if(180 == Angle1 + Angle2 + Angle3):
    print(f'The Triangle is valid.')
else:
    print(f'The Triangle is invalid.')