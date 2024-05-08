from cs50 import get_int

height = 0
while height < 1 or height > 8:
    height = get_int("Height: ")
num_spaces = height - 1
num_boxes = height - num_spaces
for i in range(height):
    print((num_spaces * " ") + (num_boxes * "#"))
    num_spaces -= 1
    num_boxes += 1