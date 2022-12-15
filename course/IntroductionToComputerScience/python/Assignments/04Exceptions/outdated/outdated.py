#   Missing to remove : September 8 1994, how do i do that?
def main():

    '''
        #   Author : krigjo25
        #   Date : .09-22

        #   Prompting the user for a date
        #   Month-Day-Year formatted ( 1/8/1636 / January 8, 1912)

        #   Outputs the same date in YYYY-MM-DD format.
        #   Prompting the user again if the date is not valid

        ##  What should i allow?
        # Alpha Dates, numeric dates
        #   May 1, 1994 / 1/9/1919
        How should i proceed to allow Alpha dates?

    '''

    #   Initializing lists

    month = [
                '', 'January', 'February',
                'March', 'April', 'May',
                'June', 'Juli', 'August',
                'September', 'October', 'November', 'December']

    #   Initializing variables
    string = ''

    while True:
        try:

            #   Prompting the user
            prompt = input('date : ').strip()

            if ',' in prompt:

                prompt = prompt.replace(',', '').rsplit(' ')

                if prompt[1] in month: raise TypeError()

            elif '/' in prompt :

                prompt = prompt.rsplit('/')

                if prompt[0] in month:
                    raise TypeError()

            else:
                raise TypeError()

        except Exception as e: continue

        else:

            if prompt[0] in month:
                m = month.index(prompt[0])
                if int(prompt[1]) > 31 : continue

            #   examine the list for date values is above a given value
            elif int(prompt[0]) > 12: continue
            elif int(prompt[1]) > 31: continue

            else:

                m = prompt[0]

            d, y = prompt[1], prompt[2]

            return print(f'{y}-{str(m).zfill(2)}-{d.zfill(2)}')

main()