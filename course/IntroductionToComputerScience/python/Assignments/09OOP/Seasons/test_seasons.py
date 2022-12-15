#   Testing dates

# Importing libraries
import pytest
from seasons import BirthDate

def test_BirthDate():

  assert BirthDate('1994-02-25') == 'Fifteen million, one hundred fourteen thousand, two hundred forty minutes'

  return