months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    # Prompt user to input date
    date = input("Date: ").strip()
    # Check if month is numeric
    if date[0].isnumeric():
        # Check if date was inputted correctly
        try:
            month, day, year = date.split("/")
        # If not entered correctly prompt again
        except:
            pass
    # Check if month is alphabetic
    elif date[0].isalpha():
        # Check if date was inputted correctly
        try:
            month, day, year = date.split(" ")
            if month in months and "," in day:
                # Strip trailing comma from day
                day = day.rstrip(",")
                # Change month to numeric format
                month = months.index(month) + 1
            else:
                continue
        # If error, prompt again
        except:
            pass

    # Convert variables to ints
    try:
        month, day, year = int(month), int(day), int(year)
        if month <= 12 and day <= 31:
            break
    except NameError:
        pass

# Print out correctly formatted date
print(f"{year}-{month:02}-{day:02}")