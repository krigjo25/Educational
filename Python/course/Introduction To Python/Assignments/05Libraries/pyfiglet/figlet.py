#   Importing responsories
import sys

#   Importing pyfiglet
from pyfiglet import Figlet, FontNotFound

#   Initializing a list


def PyFiglet():

    arg = ['-f', '--font']
    f = Figlet()

    try :

        if len(sys.argv) > 1 and sys.argv[1] in arg:
            f = Figlet(font=sys.argv[2])
            prmpt = input('prompt : ')
            print(f.renderText(prmpt))
            sys.exit()

    except (FontNotFound, ValueError) as e:

        #   Exception error
        sys.exit(f'Invalid usage')

    else:
        if len(sys.argv) == 1:
            prmpt = input('prompt:')
            print(f.renderText(prmpt))

        sys.exit('Invalid usage')


PyFiglet()