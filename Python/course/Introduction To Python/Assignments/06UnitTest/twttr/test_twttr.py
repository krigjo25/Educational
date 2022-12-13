#   Testing
#   Imporing responsories
import pytest

from twttr import shorten


    #   Preparing the lowerCapitalization test

def test_func():

    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'

    #   Raise AssertionError
    if shorten('tw3tt3r') == 'twttr': raise AssertionError
    if shorten('.t.w.i.t.t.e.r') == 'twttr': raise AssertionError


if __name__ == "__main__":
    test_func()