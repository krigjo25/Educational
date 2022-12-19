#   Importing responsories

from fuel import convert, gauge
import pytest

def test_Convert():

    #   Combining values to check if convert outputs numbers
    assert convert('1/100') == 1
    assert convert('50/100') == 50
    assert convert('99/100') == 99

def test_Gauge():

    #   Combining values to check if gauge is not buggy
    assert gauge(0) == 'E'
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'
    assert gauge(100) == 'F'
    assert gauge(50) == '50%'

#   Raise Exceptions
def test_raiseZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

def test_raiseValueError():
    with pytest.raises(ValueError):
        convert('2/1')