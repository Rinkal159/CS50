import csv
import sys

def main():

    #  Check for correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python filename.py database.csv sequence.txt")
        sys.exit(1)

    #  Read database CSV file
    data = []  # list to store each person's data

    with open(sys.argv[1], "r") as databaseFile:
        database = csv.DictReader(databaseFile)
        fieldNames = database.fieldnames  # column names (name, AGATC, AATG, etc.)

        for row in database:
            data.append(row)  # store each row as a dictionary

    #  Read DNA sequence file
    with open(sys.argv[2], "r") as sequenceFile:
        sequence = sequenceFile.read()  # full DNA string

    #  Find longest match for each STR
    match = {}  # dictionary to store STR counts

    # skip index 0 because it's "name"
    for i in range(1, len(fieldNames)):
        str_name = fieldNames[i]
        score = longest_match(sequence, str_name)
        match[str_name] = score

    #  Compare with database to find matching person
    found = False  # track if any match is found

    for row in data:
        isMatched = True  # assume match initially

        for i in range(1, len(fieldNames)):
            str_name = fieldNames[i]

            # convert CSV value to int before comparing
            if int(row[str_name]) != match[str_name]:
                isMatched = False
                break  # stop checking this row

        # if all STRs match
        if isMatched:
            print(row["name"])
            found = True
            break  # stop after finding first match

    #  If no match found
    if not found:
        print("No match")


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # check every starting position in sequence
    for i in range(sequence_length):

        count = 0

        # keep checking consecutive repeats
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            # if match found, increase count
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        # update longest run
        longest_run = max(longest_run, count)

    return longest_run


# run program
main()
