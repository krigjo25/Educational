#   faces.py

#   Defining Convert
def Convert():

    #   Prompting the user
    a = input('')

    #   Replacing ':)'
    a = a.replace(':)', '\U0001F642')
    a = a.replace(':(', '\U0001F641')


    #   Returning and printing
    return print(f'{a}')

Convert()