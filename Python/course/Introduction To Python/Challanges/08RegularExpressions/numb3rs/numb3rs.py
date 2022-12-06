import re
import sys

def main():

    """

    #   Author :    krigjo25
    #   Date :      13.09-22

    #   Calling the Ipv4Validation function

    """

    validation = validate(input('IPv4 Address:'))
    if validation == True: print('Valid')
    else: print('Invalid')


def validate(ip):

    '''

        #   Author :    krigjo25
        #   Date :      07.11-22

        #   Initializing a list & Iterate through the list
        #   Validating IPv4 Address, to accept only numbers & dot notation
        #   Numbers can not be followed by 0s

    '''
    try:

        #   1   Validating Ipv4 Address to accept only numbers and notations

        #   Initialize a list & variables
        if ':' in ip: ipv4 = [i for i in str(ip).split(':')]
        else: ipv4 = [i for i in str(ip).split('.')]



        # iterate through the list
        for i in ipv4:

            if i.isalpha() or i >= '256': return False
            elif re.search(r'(^[0][0-9]$)',i): return False

        return True

    except Exception as e: return e

if __name__ == "__main__":
    main()
