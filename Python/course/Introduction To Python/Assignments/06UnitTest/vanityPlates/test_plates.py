#   Importing responsories

from plates import is_valid
import pytest


def AlphanumericCheck():

    #   Checking if either digits or letters can exteed over 7
    if is_valid('1234AAAA'): return False
    elif is_valid('AA12AA'): return False
    elif is_valid('AAAA01'): return False
    elif is_valid('AA01AA'): return False
    elif is_valid('01AA22'): return False
    elif is_valid('AAA123'): return True


def CheckSymbol():

    #   Checking if the vanity plates accepts Symbols
    if is_valid('@.AA12'): return False
    elif is_valid('AA}]12'): return False
    elif is_valid('AA12/-'): return False
    elif is_valid('AA()'): return False
    elif is_valid('AAAAAA'): return True


def AlphaLengthCheck():

    #   Checking if either digits or letters can exteed over 7

    if is_valid('A'): return False
    elif is_valid('AAAAAAA'): return False
    elif is_valid('1234567'): return False
    elif is_valid('12'): return False
    else:
        return True


def test_BaseTest():

    if CheckSymbol() != True: raise AssertionError
    if AlphanumericCheck() != True:raise AssertionError
    if AlphaLengthCheck() != True:raise AssertionError



if __name__ == "__main__":
    test_BaseTest()