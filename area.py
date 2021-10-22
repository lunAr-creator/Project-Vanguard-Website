cost_per_meter_squared = float(input("Cost per meter squared: "))
width = float(input("Width of carpet needed: "))
length = float(input("Length of carpet needed: "))

area = width*length
full_cost = area*cost_per_meter_squared

print("The total area is " + str(area) + ". This will cost £" + str(full_cost) + " to buy carpet at " + str(cost_per_meter_squared) + " per meter squared.\n")
