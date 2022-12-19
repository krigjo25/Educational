import inflect

def main():

    #   Initializing libraries
    inf = inflect.engine()
    name = []

    #   Initializing variables

    #   Creating a loop to iterate through the program
    while True:

        try:
            #   promting the user for input
            x = str(input('name :')).capitalize()


        except EOFError:
            break

        else:
            #   Handling the string
            if len(x) != 0:
                name.append(x)

    print(f'Adieu, adieu, to {inf.join(name, final_sep=",")}')


main()
