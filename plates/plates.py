def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Check for proper length and if alphanumeric
    if plate.isalnum() == False or len(plate) < 2 or len(plate) > 6:
        return False
    # Check if first 2 letters are alphabetic
    if plate[0:2].isalpha() == False:
        return False
    # Check for numbers
    numbers = False
    for ch in plate:
        # If character is alphabetic and no numbers have been found
        if ch.isalpha() and numbers == False:
            continue
        # If the character is a digit, not numbers have been found
        elif ch.isdigit():
            # If this is the first digit and it is a 0, return False
            if int(ch) == 0 and numbers == False:
                return False
            # Otherwise all is good, continue iterating
            elif numbers == False:
                numbers = True
        # If the character is alphabetic and numbers have already been found, return False
        elif ch.isalpha() and numbers == True:
            return False
    # Return True if none of the above conditions h
    return True
main()