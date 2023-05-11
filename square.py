"""
Mailing Delgado Medina
N02005278
"""

# Must ask for customer name
name = input('What is the name of the customer? ')
# Must ask for customer address
address = input('What is the address of the customer? ')
# Must ask for the dimension of the room in feet
one_side_of_the_room_size = eval(input('What is the size of 1 side of the room (in feet)?'))
# It should determine the cost to put the flooring in the room

#area = side1 ^ 2
area = one_side_of_the_room_size ** 2

# Flooring material cost 2.00 is beign written in upper case snake case because is a constant
FLOORING_MATERIAL_COST = 2.00

# Estimated cost for flooring material calculation 
total_flooring_material_cost = area * FLOORING_MATERIAL_COST

# Installation cost 1.50 is beign written in upper case snake case because is a constant
INSTALLATION_COST = 1.50

# Estimated cost for installation cost calculation
total_installation_cost = area * INSTALLATION_COST

# Total estimate calculation adding installation cost + flooring material cost
total_estimate = total_installation_cost + total_flooring_material_cost

#This will print a blank line
print("\n")

# Estimate Receipt
print('Estimate for ', name)
print(address)

#This will print a blank line
print("\n")

print(f'Square room with area of {area:.2f} square feet')
print(f'Estimated cost for flooring material is ${total_flooring_material_cost:.2f}')
print(f'Estimated cost for installation is ${total_installation_cost:.2f}')
print(f'Total estimate is ${total_estimate:.2f}')

#This will print a blank line
print("\n")