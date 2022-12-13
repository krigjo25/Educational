#   Import
#   Importing responsories
import socket as s
from http.client import HTTPConnection
from urllib.parse import urlparse
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

class rpChecker():

    def ArgumentConstructor(self):

        '''Constructing the argparser'''
        parser  = ArgumentParser(prog = 'SC Checker', formatter_class= ArgumentDefaultsHelpFormatter, description= 'Site Connectivity Checker', epilog= 'Developed by @krigjo25')
        #   Initializing arguments to be used
        parser.add_argument('-if', '--inputfile', help =' Enter the path to the file', action='store_true')
        parser.add_argument('-u', '--urls', help ='urls to check', action='store_true')
        parser.add_argument('-a', '--a', help ='', action='store_true')
        
        arg = parser.parse_args()
        return arg

    def main(self):

        arg = self.ArgumentConstructor()
        if arg :
            if arg == '-u' or arg == '--urls': return self.CheckUrlConnection(arg)
            #elif arg == '-if' or arg == '--inputfile': return self.CheckPath(arg)
            #else: return self.CheckA(arg)
        return

    def CheckUrlConnection(self, *urls):

        return urls

if __name__ == '__main__':
    rp = rpChecker()
    rp.main()