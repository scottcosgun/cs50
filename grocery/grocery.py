# Initialize dict for grocery list:
grocery = {}

while True:
    try:
        # Input item name, uppercase it
        item = input().upper()
        # Add item to list if it does not yet exist
        if item not in grocery:
            grocery[item] = 1
        # If already in list, increase quantity by 1
        else:
            grocery[item] += 1
    # Handle control-d exception
    except EOFError:
        # Print blank line and break out of loop
        print("\n")
        break

# Sort dictionary alphabetically
sorted = sorted(grocery.items())
sorted_grocery = dict(sorted)
# Iterate over keys in sorted dict
for item in sorted_grocery:
    print(f"{sorted_grocery[item]} {item}")