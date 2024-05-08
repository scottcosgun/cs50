import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    # Read database file into a variable
    with open(sys.argv[1], "r") as file_csv:
        reader = csv.DictReader(file_csv)
        database = list(reader)

    # Read DNA sequence file into a variable
    with open(sys.argv[2], "r") as file_txt:
        sequence = file_txt.read()

    # Find longest match of each STR in DNA sequence
    # Iterate through subsequences from header of CSV file
    # Store each subsequence in a dictionary
    match = {}
    for subsequence in reader.fieldnames[1:]:
        match[subsequence] = longest_match(sequence, subsequence)

    # Check database for matching profiles

    counter = 0
    # Iterate through database
    for i in range(len(database)):
        # Iterate through subsequences
        for subsequence in match:
            # If the number of repeats matches the database
            if int(database[i][subsequence]) == match[subsequence]:
                counter += 1
        # If all STRs line up to the person in the database, print their name and exit
        if counter == len(match):
            person = database[i]["name"]
            print(person)
            sys.exit()
        # If not a match, start over
        else:
            counter = 0
    # Print "No match" if no match is found after iterating through database
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
