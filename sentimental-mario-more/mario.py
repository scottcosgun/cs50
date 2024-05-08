from cs50 import get_int

# Prompt user for height 1-8, inclusive, rejecting any input outside of this range
height = 0
while height < 1 or height > 8:
    height = get_int("Height: ")
# Initialize variable for number of spaces and boxes to print in first row
num_spaces = height - 1
num_boxes = height - (height - 1)
# Iterate through each row top to bottom, printing out pyramid
for i in range(height):
    print((num_spaces * " ") + (num_boxes * "#") + "  " + (num_boxes * "#"))
    num_spaces -= 1
    num_boxes += 1