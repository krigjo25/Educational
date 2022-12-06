# Importing responsories
import re,sys

def main():
    print(convert(input("Hours: ")))


def convert(arg):

  '''
    #   Author    Krigjo25
    #   Date :    05.11-22
    #
    #   1. implement a function called convert that expects a str in either of the 12-hour formats below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
    #   2. Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
    #   3. Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.
    #   4. Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.)
    #   5. But do not assume that someone’s hours will start ante meridiem and end post meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
  '''

  #
  try :

    #   Checking if there is any space after the clock
    match = r'([0-9]\S[a-zA-Z])'

    if re.search(match, arg): raise ValueError()
    if 'AM' not in arg and 'PM' not in arg or '-' in arg: raise ValueError()

    #   Initializing a list
    arg = [i for i in str(arg).split(' ')]

  except Exception as e:
     sys.exit('ValueError')

  else:

    #   When the user enters only a digit
    if ':' not in arg[0]:

      if 'AM' in arg[1]:

        arg = [i for i in arg if re.search(r'[0-9]', i)]

        #   Converting midnight
        if arg[0] == '12': arg[0], arg[1] = f'00:00', f'{arg[1]}:00'
        else:arg[0], arg[1] = f'{arg[0].zfill(2)}:00', f'{int(arg[1]) + 12}:00'

      elif 'PM' in arg[1]:

        arg = [i for i in arg if re.search(r'[0-9]', i)]
        if arg[0] == '12': arg[1], arg[0] = f'{arg[1]}:00', f' 00:00'
        else: arg[1], arg[0] = f'{arg[1].zfill(2)}:00', f'{int(arg[0]) + 12}:00'

    #   When the user enters multiple digits including semicolon
    else:

      if 'AM' in arg[1]:

        # Initializing a list
        arg = [i for i in arg if re.search(r'^\d', i)]

        #   Converting 12 AM
        if arg[0][0] == '1' and arg[0][1] == '2': arg[0]= f'00{arg[0][2:]}'
        elif int(arg[0][2]) > 5 or int(arg[1][2]) > 5: raise ValueError('ValueError')
        else :arg[0], arg[1] = f'{arg[0][0].zfill(2)}:00', f'{int(arg[1][0]) + 12}{arg[1][1:]}'


      elif 'PM' in arg[1]:

        # Initializing a list
        arg = [i for i in arg if re.search(r'^\d', i)]

        #   Converting 12 PM to
        if arg[1][0] == '1' and arg[1][1] == '2': arg[1]= f'00{arg[0][2:]}'
        elif int(arg[0][2]) > 5 or int(arg[1][2]) > 5: raise ValueError('ValueError')
        else: arg[1], arg[0] = f'{arg[0][0].zfill(2)}{arg[0][1:]}', f'{int(arg[1][0]) + 12}{arg[1][1:]}'

  return f'{arg[0]} to {arg[1]}'

if __name__ == "__main__":
    main()