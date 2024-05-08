import sys
import csv
from tabulate import tabulate

# Check for proper # command line arguments
if len(sys.argv) == 1:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")
# Check if csv file
elif sys.argv[1].strip().endswith(".csv") == False:
    sys.exit("Not a csv file")

# Initialize list and key for pizza type
pizza = []
firstcod = "Pizza"

# Try opening the file
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        if sys.argv[1].strip().startswith("sicilian") == True:
            first = "Sicilian Pizza"
        elif sys.argv[1].strip().startswith("regular") == True:
            first = "Regular Pizza"
        for row in reader:
            # Create list of dictionaries
            pizza.append({first: row[first], "Small": row["Small"], "Large": row["Large"]})
# Handle Exception
except FileNotFoundError:
    sys.exit("File not found")

# Print tabulated list in grid format
print(tabulate(pizza, headers="keys", tablefmt="grid"))