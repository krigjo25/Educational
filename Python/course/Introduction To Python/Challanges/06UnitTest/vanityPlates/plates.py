def main():

        plate = input('Plate: ').upper()
        plate = str(plate)

        if is_valid(plate):
            print('valid')

        else:
            print('invalid')



def is_valid(s): return PlateValidation(s)


def PlateValidation(plate):

    #   Initializing variables


    #   Iterating throught the plate
    if CheckLengthAndSymbols(plate):
        if CheckTheNumbers(plate):
            if PlateDesign(plate): return True
            else : return False
        else: return False
    else: return False


def CheckLengthAndSymbols(arg):

    #   Checking if there is maximum of 6 character
    if len(arg) <= 6 and len(arg) > 1:

        #   Return True if arg is only number and letters
        if str(arg).isalnum(): return True
        else: return False

    else: return False

def CheckTheNumbers(arg):

    '''
        Checking for the first digit in the string,
        if the number starts with 0 return false.
    '''

    #   Iterating through the argument
    for i in str(arg):

    #   Checking the first Integer
        if i.isdigit():
            if i.startswith('0'): return False
            else: return True

        else: continue

    return True

def PlateDesign(arg):

    '''
                    PlateDesign
        If the numbers are in the middle of the prompt
        the user will recive an error.

    '''

    #   Checking if the first Two Characters is letters

    if str(arg[0:2]).isalpha():

        #   Checking if the numbers is at the end
        a = len(arg)

        if str(arg[2:]).isnumeric():return 'True'
        elif str(arg[3:]).isnumeric(): return 'True'
        elif str(arg[4:]).isnumeric(): return 'True'
        elif str(arg).isalpha(): return 'True'
        else: return False

    else: return False
if __name__ == "__main__":
    main()