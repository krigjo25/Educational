from project import SCChecker
import pytest


def test_pingConnection():
        
        checker = SCChecker
        assert checker.UrlParse('Google.com') == 'online'
