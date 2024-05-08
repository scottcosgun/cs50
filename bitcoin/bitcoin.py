import requests
import sys

# Gather user input for # bitcoins in command-line and try to convert to a float
# Check for only 1 argument
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
try:
    bitcoin = float(sys.argv[1])
except IndexError:
    sys.exit("Missing command-line argument")
# Check to ensure number is entered
except ValueError:
    sys.exit("Command-line argument is not a number")

# Query for bitcoin price
try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
except requests.RequestException:
    sys.exit("Unable to complete request at this time")

# Get JSON and convert to python dictionary
info = r.json()

# Index into dictionary to get the current price of bitcoin as a float
usd = info["bpi"]["USD"]["rate_float"]

# Calculate price of purchasing x bitcoin in USD and print
price = usd * bitcoin
print(f"${price:,.4f}")