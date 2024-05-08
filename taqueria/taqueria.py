menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Set total = 0
total = 0.00
# Infinite loop
while True:
    # try asking the user to input an item from the menu
    try:
        item = input("Item: ").title()
    # Handle exception of control-d
    except EOFError:
        print()
        break
    # Check if titled item is in menu
    if item in menu:
        # Add to total and print
        total += menu[item]
        print(f"Total: ${total:.2f}")