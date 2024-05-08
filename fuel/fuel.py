while True:
    # Prompt user for fraction
    fuel = input("Fraction: ")

    # Try splitting and converting x and y to ints
    try:
        # Split fraction at the /
        x, y = fuel.split("/")
        # Convert x and y to ints
        x = int(x)
        y = int(y)
        # Restart if x > y
        if x > y:
            continue
        else:
            # Calculate fraction and break out of while loop
            percentage = round(100 * (x/y))
            break
    # Handle exceptions
    except (ValueError, ZeroDivisionError):
        continue

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")