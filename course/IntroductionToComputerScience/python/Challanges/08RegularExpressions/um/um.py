import re
import sys

def main():
    print(count(input("Text: ").lower()))


def count(arg):

    '''
        #   Author :    Krigjo25
        #   Date   :    05.11-22

        #   1. Implement a function called count that expects a line of text as input as a str and returns, as an int.
        #   2. the number of times that “um” appears in that text, case-insensitively, as a word unto itself, not as a substring of some other word.
        #   3. For instance, given text like hello, um, world, the function should return 1. Given text like yummy, though, the function should return 0.
    '''

    #   Finding every 'um'
    match = r'^(um)'

    #   Initializing a list
    counter = 0
    arg = [i for i in str(arg).lower().split(' ')]

    #   Looping through the argument of words
    for i in arg:

        #   Matching the regex for each word in the list
        if re.search(match, i):
            if not 'mm' in i:counter += 1

    #   Delete lists
    del arg

    return counter

if __name__ == "__main__":
    main()