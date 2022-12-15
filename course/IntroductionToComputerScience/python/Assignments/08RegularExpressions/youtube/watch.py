# Importing responsories

import sys, re

def main():
  print(parse(input('HTML:')))

def parse(arg):

  '''
  #   Author : krigjo25
  #   Date :  1.11-22

  #   Expects a str of HTML as input.
  #   Extracts any YouTube URL and return the shorter youtu.be equivalent as a str.
  #   Expect that any such URL will be in one of the formats below.
  #   Assume that the value of src will be surrounded by double quotes.
  #   And assume that the input will contain no more than one such URL. If the input does not contain any such URL at all, return None.
  '''

  #   Initializing a no no list
  nonolist = [  '"', '=', 'src',
                'www', '.', '/', '>', '<',
                ':','youtube', 'com',
                'https', 'http', 'iframe','embed']

  arg = [i for i in str(arg).rsplit(' ')]

  match = r'^src='

  for i in arg:
    regex = re.search(match, i)

    if regex : arg = i

  if 'youtube' not in arg: return None

  for i in nonolist:
    arg= str(arg).replace(i,'')

  return f'https://youtu.be/{arg}'

if __name__ == '__main__':
  main()