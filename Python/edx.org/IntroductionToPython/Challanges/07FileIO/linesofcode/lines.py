#   Importing Python responsories
import sys

def ReadLines():

    """
        #   Author :    krigjo25
        #   Date :      26.08-22

        #   Checking wehter cmdline conditions is accurate.
        #   Opening a file, remove any white spaces
        #   Returning an exception if the file does not exist
        #   Removing any comments in the file.
        #   Return number of lines.

    """
    try :

        if len(sys.argv) < 2: sys.exit('Too few command line arguments')
        elif len(sys.argv) >= 3: sys.exit('Too many Command line arguments')
        elif '.py' not in sys.argv[1]:sys.exit('Not a python file')

    except FileNotFoundError as e:
        print(e)

    else:

        lines = []
        with open(f'{sys.argv[1]}', 'r') as f:

            #   iterating through the file and remove any white space
            lines = [str(i).lstrip() for i in f.readlines() if i.strip()]

        f.close()

        #   Iterate through list, remove comments
        lines = [i for i in lines if not i.startswith('#')]

        return print(len(lines))


ReadLines()