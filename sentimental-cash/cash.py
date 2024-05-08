from cs50 import get_float

change = 0.00
# Check to make sure user inputs a positive number
while change <= 0:
    change = get_float("How much change is owed? ")
# Convert change to only cents
change = change * 100
# Initialize coins variable to zero
coins = 0
# Get number of quarters, add to coins total, subtract quarters from change total
while change >= 25:
    coins += 1
    change -= 25
# Repeat for dimes
while change >= 10:
    coins += 1
    change = change - 10
# Repeat for nickels
while change >= 5:
    coins += 1
    change -= 5
# Repeat for pennies
while change >= 1:
    coins += 1
    change -= 1
# Print the minimum number of coins the customer is owed
print(coins)
