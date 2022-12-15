#   Importing Python responsories
import os
import sys
import csv

def main():

    """
        #   Author :    krigjo25
        #   Date :      30.08-22

        #   Expects the user to provide two command-line arguments
        #   If the user does not provide exactly two command-line arguments
        #   if the first cannot be read, the program should exit via sys.exit with an error message.

    """

    #   Combining values to check the cmdline values.
    if len(sys.argv) < 3: sys.exit('Too few command line arguments')
    elif len(sys.argv) >= 5: sys.exit('Too many Command line arguments')
    elif '.csv' not in sys.argv[1]:sys.exit('Not a CSV file')
    else: return CSVWriter()

def CSVWriter():

    """
        #   Author :    krigjo25
        #   Date :      06.09-22

        #   the name of an existing **CSV file** to read as input, whose columns are assumed to be, in order, name and house
        #   the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.
        #   Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name

    """

    #   Initializing a list
    student = []

    #   Open the csv file & write to a new CSV file
    with open(f'{sys.argv[1]}') as f, open(f'{sys.argv[2]}', 'w') as w:

        try:

            #   Iterating through the CSV file & sorting the name by first-/lastname

            for i in csv.DictReader(f):

                #   Handling the strings
                j,k = i['name'].split(',')
                j,k = j.lstrip(), k.lstrip()

                #   Appending to list
                student.append({'first': k, 'last':j, 'house':i['house']})

            #   Writing to another file


            columns = ['first', 'last', 'house']

            #   Create a header
            cw = csv.DictWriter(w, fieldnames= columns)
            cw.writeheader()

            #   Write the rows
            cw.writerows(student)


            #   Close the file
            f.close()
            w.close()

    #   Except an exception if occures
        except FileNotFoundError as e:
            sys.exit('Could not read the CSV')
main()