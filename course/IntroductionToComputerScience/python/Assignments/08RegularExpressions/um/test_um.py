# Importing responsories

import pytest
from um import count

def test_um():


    # Main function
    assert MainTest() == True

def MainTest():

    #   Creating variables to test

    a = 'Um, thanks for the album'  #   1
    b = 'Um, thanks, um..'          #   2
    c = 'um?.. Its not an Umbrella' #   1

    #   Counting how many 'um'
    assert count(a) == 1
    assert count(b) == 2
    assert count(c) == 1

    return True


if __name__ == '__main__':
  test_um()