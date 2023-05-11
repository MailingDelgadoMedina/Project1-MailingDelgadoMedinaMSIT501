# import the libraries needed
from math import pi

# Must ask for customer name
name = input('What is the name of the customer? ')
# Must ask for customer address
address = input('What is the address of the customer? ')
# Must ask for the dimension of the room in feet
one_side_of_the_room_size = eval(input('What is the size of 1 side of the room (in feet)? '))
# It should determine the cost to put the flooring in the room
radius = one_side_of_the_room_size / 2
# circle = area = radius^2 * pi
area = pi * radius ** 2
# Flooring material cost 2.00
flooring_material_cost = 2.00
# Estimated cost for flooring material
total_flooring_material_cost = area * flooring_material_cost
# Installation cost 1.50
installation_cost = 1.50

total_installation_cost = area * installation_cost

total_estimate = total_installation_cost + total_flooring_material_cost

print('Estimate for ', name)
print(address)


print(f'Circular room with area of {area:.2f} square feet')
print(f'Estimated cost for flooring material is ${total_flooring_material_cost:.2f}')
print(f'Estimated cost for installation is ${total_installation_cost:.2f}')
print(f'Total estimate is ${total_estimate:.2f}')
