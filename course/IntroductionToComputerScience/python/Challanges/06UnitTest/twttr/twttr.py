#   Initializing a list
#   Imporing responsories

#   Initializing a list

def main():

        #   Promting the user to input a text
        try :
            x = str(input('prompt :'))
            x = shorten(x)

        except (ValueError, TypeError) as e:
            print (e)

        else:
            #   Printing the output
            print(x)
        return

def shorten(arg):

    #   Initializing variables
    string = ''
    arg = str(arg)

    #   Initializing a list with vowels
    x = [   'a','e','i','o','u'
            'A','E','I','O','U']

    #   Iterating through the argument
    for i in arg:

        if i not in x and i.isalpha():
            string += i

    return string

if __name__ == '__main__':
    main()