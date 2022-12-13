from bank import value
import pytest

def test_func():

    assert value('hello') == 0
    assert value('hey') == 20
    assert value('else') == 100


    #   Raise AssertionError


    if value('hey') != 20: raise AssertionError
    if value ('Hey') != 20: raise AssertionError
    if value('Hello') != 0: raise AssertionError
    if value('hello') != 0: raise AssertionError
    if value('Else') != 100: raise AssertionError
    if value('else') != 100: raise AssertionError


if __name__ == "__main__":
    test_func()