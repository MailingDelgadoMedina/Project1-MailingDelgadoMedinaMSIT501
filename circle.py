"""
 Mailing Delgado Medina
 N02005278
"""

# import the libraries needed in this case pi from math
from math import pi

# Must ask for customer name
name = input('What is the name of the customer? ')
# Must ask for customer address
address = input('What is the address of the customer? ')
# Must ask for the dimension of the room in feet
diameter = eval(input('What is the diameter of the room (in feet)? '))

# It should determine the cost to put the flooring in the room

# calculate the radius by dividing the diameter by 2
radius = diameter / 2
# calculate the area  area = radius^2 * pi
area = pi * radius ** 2

# Flooring material cost 2.00 is being written in upper case snake case because is a constant
FLOORING_MATERIAL_COST = 2.00

# Calculate the estimated cost for flooring material
total_flooring_material_cost = area * FLOORING_MATERIAL_COST

# Installation cost 1.50 is being written in upper case snake case because is a constant
INSTALLATION_COST = 1.50

# Calculate the estimated installation cost
total_installation_cost = area * INSTALLATION_COST

#Calculate the total estimate
total_estimate = total_installation_cost + total_flooring_material_cost

#This will print a blank line
print("\n")

#Estimate Receipt
print('Estimate for ', name)
print(address)

#This will print a blank line
print("\n")

print(f'Circular room with area of {area:.2f} square feet')
print(f'Estimated cost for flooring material is ${total_flooring_material_cost:.2f}')
print(f'Estimated cost for installation is ${total_installation_cost:.2f}')
print(f'Total estimate is ${total_estimate:.2f}')

#This will print a blank line
print("\n")