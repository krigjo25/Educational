#MealTime.py
def MealTimeConverter(x):


    #   Checking the condition of x
    if x > 6.9 and x <= 8: print('Breakfast time')
    elif x >  12 and x <= 13: print('lunch time')
    elif x > 18 and x <= 19: print('Dinner time')


    #   Return the result

    return x


def MealTime():

    # Prompt the user for time
    prmpt = input('Insert time : ')

    #   Handling the string
    x, y = prmpt.split(':')

    #   Converting the string into a decimal number
    x = float(x)
    y = float(y)

    #   Dividing the remaining minutes into a decimal place
    y /= 60

    #   Adding the result into x
    x += y

    #   Call MealTimeConverter
    MTC = MealTimeConverter(x)
    #   Return the result
    return MTC

if __name__=='__main__':MealTime()