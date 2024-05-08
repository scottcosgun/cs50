# E = mc^2

# Prompt user for mass, in kg
mass = input("Enter mass as an int, in kg: ")
mass = int(mass)
# Store variable for c (m/s)
c = 300000000

# Perform mathematical calculation
E = (mass) * (c ** 2)
print(E)