#   einstein.py

#   Defining a function to measure the input
def EnergyMeasured():
    ''' EnergyMeasured

        The Function finds the Energy equals mass times the speed of light squared
        To find the Energy we use the formula E = mc2.
        m = Mass (kg) * s = Speed of light which is 3*10**8
    '''
    #   Initializing variables & prompt the user.
    #   Finding the output by using the
    #   Mass object
    m = int(input(''))

    # Calculating the Speed of light
    c = 3 * 10**8

    #   Calculateing the Energy of the object
    e = m * c ** 2

    #   Print out the equivalent number of Joules
    return print(e)

EnergyMeasured()