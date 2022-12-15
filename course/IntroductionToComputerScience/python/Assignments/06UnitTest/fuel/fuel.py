def main():

    #   Checking if the input contains only numbers
    x, y = input('prompt : ').split('/')

    print(convert(x,y))

def convert(arg):

    """ Converting the fraction to prosentage """

    #   Converting to int
    x,y = arg.split('/')
    x, y = int(x), int(y)

    #   Combining the values
    if y == 0: raise ZeroDivisionError('Can not be devided with zero')
    elif x > y: raise ValueError('x can not be greater than y')

    else:
        #   Finding the procentage of the fraction
        x = (x / y) * 100

        #   Rounding x up to the closest integer
        arg = round(x)

        if arg < 101:
            return arg

        return

def gauge(arg):

    #   Checking if the value is below 100%
    if arg > 98: return 'F'
    elif arg < 2: return 'E'
    else: return arg

if __name__ == '__main__':
    main()