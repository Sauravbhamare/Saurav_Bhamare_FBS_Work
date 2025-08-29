length = int(input("Enter length of one wall:"))
breadth = int(input("Enter breadth of one wall:"))
cost_per_unit = int(input("Enter the cost for painting per unit:"))

area_one_wall = length * breadth

total_area_all_walls = area_one_wall * 4

total_cost = total_area_all_walls * cost_per_unit

print(f'Total cost of painting interior with four equal sized wall:{total_cost}.')
