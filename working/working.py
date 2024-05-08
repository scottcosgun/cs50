import re


def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Save regex for time as variable
    regex = (r"([1-9]|1[0-2])(:[0-5][0-9])? (A|P)M")
    # Search string for correct format
    if matches := re.search(r"^" + regex + " to " + regex + "$", s):
        # Store list for captured groups
        times = matches.groups()
        # Convert to 24 hour format and return
        return f"{convert_24(times[:3])} to {convert_24(times[3:])}"

    # Raise ValueError if formatting is not not correct
    raise ValueError("Incorrect format")

def convert_24(time):
    # time[0] == hour, time[1] == minute, time[2] == A or P

    # Handle case for 12AM or 12PM
    if time[0] == "12":
        hour = '00' if time[2] == 'A' else '12'
    # Convert to 24 hour time and format to ##:##
    elif time[2] == 'A':
        hour = f"{int(time[0]):02}"
    else:
        hour = f"{int(time[0]) + 12}"
    minute = "00" if time[1] == None else f"{int(time[1].strip(':')):02}"
    # Return formatted time
    return hour + ":" + minute

if __name__ == "__main__":
    main()