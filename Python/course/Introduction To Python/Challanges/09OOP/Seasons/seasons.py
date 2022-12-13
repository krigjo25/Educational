#   Importing Responsories
import datetime, sys
import inflect

def main():
  print(BirthDate(input('Date of birth :')))

def BirthDate(arg):

    '''

        #   Author :    Krigjo25
        #   Date :      07.11-22

        #   Prompting the user for their date of birth YYYY-MM-DD
        #   Exit through sys.exit if its incorrectly formated.
        #   Caluculating how old the user is in minutes rounded to nearest integer.

        #   Printing how old they are in words.
        #   Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date.
        #   Assume that the current time is also midnight. In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date.
        #   Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
        #   Exit via sys.exit if the user does not input a date in YYYY-MM-DD format. Ensure that your program will not raise any exceptions.


    '''

    try :



      if '-' not in arg: raise ValueError('Not a valid date, use YYYY-MM-DD')

      #   Initializing variables
      today = datetime.date.today()
      arg = [i for i in str(arg).split('-')]


    except Exception as e : sys.exit(e)
    else:

      #   Finding the difference between the dates
      arg = datetime.date(int(arg[0]), int(arg[1]), int(arg[2]))
      arg = today - arg

      #   Calculating how many minutes there have been
      arg = f'{1440 * arg.days}'

      p = inflect.engine().number_to_words(arg, andword='').capitalize()
      arg = f'{p} minutes'

      #   Clean up
      del today

      return arg

if __name__ == "__main__":
  main()