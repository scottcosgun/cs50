# Get mathematical expression from user
math = input("Expression: ")

# Split the expression into variables, split by a space
x, y, z = math.split(" ")

# Convert x and y to ints
x = float(x)
z = float(z)

# Check conditions and calculate equation
if y == "+":
    answer = x + z
elif y == "-":
    answer = x - z
elif y == "*":
    answer = x * z
elif y == "/":
    answer = x / z

# Print answer onto screen
print(answer)