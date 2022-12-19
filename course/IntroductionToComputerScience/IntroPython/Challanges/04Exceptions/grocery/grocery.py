def main():

    '''

        #   Author: krigjo25
        #   Date: 20.09-22

        #   Then output the user’s grocery list in all uppercase,
        #   Sorted alphabetically by item,
        #   Prefixing each line with the number of times the user inputted that item. <br>
        #   No need to pluralize the items.
        #   Treat the user’s input case-insensitively.
    '''

    #   initializing variables
    x = 1
    dictionary = {}

    while True:

        #   Prompting the user to input, case-insensitively
        try :
            prompt = str(input('')).upper()

        #   Exception
        except EOFError as e:
            print(e)
            break


        else:

            #   Storing the prompt value
            if prompt in dictionary:

                # Counting the value up
                dictionary[f'{prompt}'] += 1

            #   Registering the key
            else:
                dictionary[f'{prompt}'] = 1

            # Sorting the dictionary alphabetical
            dictionary = dict(sorted(dictionary.items()))

    #   Print the output
    for i in dictionary :
        print(f'{dictionary[i]} {i}')

main()