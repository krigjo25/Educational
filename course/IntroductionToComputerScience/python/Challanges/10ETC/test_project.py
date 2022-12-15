from project import SCChecker
import pytest


def test_pingConnection():
        
        checker = SCChecker
        assert checker.UrlParse('Google.com') == 'online'

# cd documents/educational/course/introductiontocomputerscience/python/challanges/10etc