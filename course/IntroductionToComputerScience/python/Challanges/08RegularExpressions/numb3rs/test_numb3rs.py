import pytest
from numb3rs import validate

#   Failing to catch numb3rs.py by only checking first byte of an IPV4address
def test_IPvAddress():

    '''
        #   Author : krigjo25
        #   Date : 09-22

        #   Test
    '''

      # Initializing variables
    assert TestIpv4() == True



    return True

def TestIpv4():

    #   Initializing variables, ips to be tested
    ip = '127.0.0.1'
    ip1 = '255.255.255.255'
    ip2 = '512.512.512.512'
    ip3 = '1.2.3.1000'
    ip4 = 'cat'
    ip5 = '2.'

    # Checking the boolean value for the test
    assert validate(ip) == True
    assert validate(ip1) == True

    assert validate(ip5) == False
    assert validate(ip2) == False
    assert validate(ip3) == False
    assert validate(ip4) == False

    return True
