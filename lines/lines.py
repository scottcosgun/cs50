import sys
import csv

# Check proper number of command line arguments
if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

f = sys.argv[1].strip()

# Ensure file ends in .py
if f.endswith(".py") == False:
    sys.exit("Not a python file")

# Initialize variable to count lines
lines = 0

# Try opening the file, handle exception
try:
    with open(f, "r") as file:
        for row in file:
            # Only count lines that are not commends and that are not blank
            if row.strip().startswith("#") == False and row.strip() != "":
                lines += 1
except FileNotFoundError:
    sys.exit("File not found")

# Print number of lines of code
print(lines)