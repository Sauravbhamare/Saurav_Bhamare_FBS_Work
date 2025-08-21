L = int(input("Enter length of the Rectangle:"))
B = int(input("Enter breadth of the Rectangle:"))
R = int(input("Enter the radius of the Circle:"))

rect_area = L * B
cir_peri = 3.14 * R
cir_area = 3.14 * R **2
rect_peri = 2 * (L + B)
print(f'The perimeter of circle: {cir_peri}')
print(f'The area of Rectangle: {rect_area}')
print(f'The area of Circle: {cir_area}')
print(f'Perimeter of Rectangle is: {rect_peri}')

area = rect_area + (cir_area / 2)
peri = rect_peri + (cir_peri / 2)

print(f'Area of Diagram: {area}')
print(f'Perimeter of Diagram: {peri}')

