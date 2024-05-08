import sys

# Prompt user for card number
try:
    number = int(input("Number: "))
# Quit if number is not entirely numeric
except ValueError:
    print("INVALID")
    sys.exit(1)
# Initialize variable for card length
length = len(str(number))
# Check if length matches conditions
if length != 13 and length != 15 and length != 16:
    print("INVALID")
    sys.exit(2)

# Calculate checksum
copy = number
first_sum = 0
second_sum = 0
# Iterate through card digits
while copy != 0:
    # Add every other digit so "second_sum", starting with last digit
    second_sum += (copy % 10)
    # Remove last digit and check if any digits left
    copy = copy // 10
    if copy == 0:
        break
    # Multiply second to last digit by 2
    multiple = (copy % 10) * 2
    # If multiplied digit >= 10, split it up and add each digit to "first_sum"
    if multiple >= 10:
        a = multiple % 10
        b = multiple // 10
        first_sum += a + b
    # Otherwise add the digit to "first_sum"
    else:
        first_sum += multiple
    # Use floor division to remove last two digits from copy
    copy = copy // 10
# Calculate checksum and check if checksum % 10 == 0
total = first_sum + second_sum
if total % 10 != 0:
    print("INVALID")
    sys.exit(3)
# Convert card number to string to easily index into
number = str(number)
first = int(number[0])
second = int(number[1])
# Check if 13 digit Visa
if len(number) == 13 and first == 4:
    print("VISA")
    sys.exit()
# Check if 15 digit AMEX
elif len(number) == 15:
    if first == 3 and (second == 4 or second == 7):
        print("AMEX")
    else:
        print("INVALID")
    sys.exit()
# Check if 16 digit Mastercard or Visa
elif len(number) == 16:
    if first == 4:
        print("VISA")
        sys.exit()
    elif first == 5 and (1 <= second <= 5):
        print("MASTERCARD")
        sys.exit()
else:
    print("INVALID")
    sys.exit()