from datetime import date
import sys
import inflect


def main():
    birthdate = validate(input("Date of birth: "))
    print(f"{minutes(birthdate)} minutes")

def validate(user_date):
    # Try splitting the birthtime into y/m/d
    try:
        year, month, day = user_date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)
        # Return timedelta format of birthday
        return date(year, month, day)
    # If unable to split date, exit
    except ValueError:
        sys.exit("Invalid date. Format YYYY-MM-DD")

def minutes(birthdate):
    # Open up inflect
    p = inflect.engine()
    # Calculate the number of days that have passed between birthday and today
    difference = date.today() - birthdate
    # Convert days to minutes, in words
    return p.number_to_words((difference.days * 1440), andword="").capitalize()


if __name__ == "__main__":
    main()