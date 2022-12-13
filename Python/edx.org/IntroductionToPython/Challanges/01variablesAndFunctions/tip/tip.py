
#   TipCalculator.py
def main():

    #   Initializing the variables
    #   Asking the user for a input
    dollar = dollarsToFloat(input('How much was the meal?'))
    percent = percentToFloat(input('What procentage would you like to tip?'),)

    #   Calculate the output
    tip =  dollar * percent

    #   Returning the string
    print(f'Leave ${tip:.2f}\n')

    return


def dollarsToFloat(arg):

    #   Handling the string
    arg = str(arg).replace('$', '')
    arg = float(arg)

    #   Returning the argument
    return arg

def percentToFloat(arg):

    #   Handling the string
    arg = str(arg).replace('%', '')
    arg = float(arg)

    #   Converting to procentage
    arg /= 100

    #   Returning the argument
    return arg

main()