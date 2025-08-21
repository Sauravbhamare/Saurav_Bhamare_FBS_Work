L = int(input("Enter the length of one wall : "))
B = int(input("Enter the Breadth of one wall:"))

Area = L * B
print(f'The area of one wall is: {Area}.')

inter_cost = int(input('Enter the interior painting cost for one wall: '))
exter_cost = int(input('Enter the exterior painting cost for one  wall:'))

intercost_all = Area * inter_cost * 8
extercost_all = Area * exter_cost * 7

print(f'The cost for interior painting of all walls: {intercost_all}.')
print(f'The cost for exterior painting of all walls: {extercost_all}')
