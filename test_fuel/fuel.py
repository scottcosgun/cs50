def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        # Try splitting and converting x and y to ints
        try:
            # Split fraction at the /
            x, y = fraction.split("/")
            # Convert x and y to ints
            x = int(x)
            y = int(y)
            # Restart if x > y
            if x > y and y != 0:
                fraction = input("Fraction: ")
                continue
            else:
                # Calculate fraction and break out of while loop
                percentage = round(100 * (x/y))
                return percentage
        # Handle exceptions
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return (f"{percentage}%")

if __name__ == "__main__":
    main()