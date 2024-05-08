import inflect
import sys

p = inflect.engine()

# Initiate list
names = []

# Continuously ask for names and append them to the list until the user inputs control-d
while True:
    try:
        # Get user input
        name = input("Name: ")
        # Append to list
        names.append(name)
    except EOFError:
        # Print a new line and break out of the loop
        print()
        break

# Make grammatically correct list of names
output = p.join(names)
# Print the final output
print("Adieu, adieu, to " + output)