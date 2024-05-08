import sys
import csv

def main():
    check_command_line()

    # Initialize list
    output = []

    # Try opening file
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Split name into first and last
                last, first = row["name"].strip('"').split(",")
                # Append dictionaries to list of output
                output.append({"first": first.strip(), "last": last.strip(), "house": row["house"]})

    # Handle exception
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    # Write new csv file
    with open(sys.argv[2], "w") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def check_command_line():
    # Ensure correct # command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()