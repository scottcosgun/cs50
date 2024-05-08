def main():
    time = input("What time is it? ")
    hour = convert(time)
    if 7 <= hour <= 8:
        print("breakfast time")
    elif 12 <= hour <= 13:
        print("lunch time")
    elif 18 <= hour <= 19:
        print("dinner time")

def convert(time):
    # Split time into hours and minutes
    hours, minutes = time.split(":")
    # Convert str values to float
    hours = float(hours)
    minutes = float(minutes)
    # Calculate hour of the day as a float and return
    decimal = minutes / 60
    hour = hours + decimal
    return hour

if __name__ == "__main__":
    main()