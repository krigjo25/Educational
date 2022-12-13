#   Importing Python responsories
import sys
import csv

#   Tabulate responsory
from tabulate import tabulate

def main():

    """
        #   Author :    krigjo25
        #   Date :      30.08-22

        #   Checking wether cmdline conditions is accurate.
        #   Except a FileNotFoundError if not found

    """

    #   Combining values to check the cmdline values.
    if len(sys.argv) < 2: sys.exit('Too few command line arguments')
    elif len(sys.argv) >= 3: sys.exit('Too many Command line arguments')
    elif '.csv' not in sys.argv[1]:sys.exit('Not a CSV file')
    else: return CSVReader()

def CSVReader():

    """
        #   Author :    krigjo25
        #   Date :  30.08-22

        #   Opening a CSV file, using 'csv' library to generate a list.

        #   Using tabulate to print the CSV table using gird format


    """
    try:

        #   Open the csv file
        with open(f'{sys.argv[1]}', 'r') as f:

            #   Iterate through the csv file
            table = [i for i in csv.DictReader(f)]

            #   print the tabulated table
            return print(tabulate(table, headers = "keys", tablefmt = 'grid'))

    except FileNotFoundError as e: sys.exit(e)

main()