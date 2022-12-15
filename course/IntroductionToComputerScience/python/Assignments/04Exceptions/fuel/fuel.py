def main():

    #   Prompting the user for a input
    while True:

        try:

            x, y = input('prompt : ').split('/')

                    #  Converting string into into
            x, y = int(x), int(y)

            #   Finding the procentage of the fraction
            x = (x / y) * 100

        except (ValueError, ZeroDivisionError) as e:
            print(e)
            continue

        else:
            #   Converting Fraction to integer

            x = round(x)

            #   Checking if the value is below 100%
            if x < 101:

                if x > 98:
                    print('F')
                elif x < 2:
                    print('E')
                else:
                    print(f'{x}%')

                #   Breaking out of the loop
                break

            else :
                continue

    return

main()