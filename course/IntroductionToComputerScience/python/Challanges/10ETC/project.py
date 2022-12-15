#   Import
import sys
import requests as r

#   Importing responsories
from pythonping import ping
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

class CommandlineInterface():
    
    '''
        The command line Interface
    '''

    def CommandLineOptions(self):

        '''Constructing the argparser'''
        parser  = ArgumentParser(prog = 'Site Connectivity Checker', formatter_class= ArgumentDefaultsHelpFormatter, description= 'Site Connectivity Checker', epilog= 'by @krigjo25')

        #   Initializing command line arguments
        parser.add_argument('-inf', '--inputfile', dest = 'inf', help =' Enter the path to the file', action = 'append')
        parser.add_argument('-p', '--ping', dest = 'ping', help ='Ping a website', action = 'append')
        parser.add_argument('-u', '--urls', dest = 'urls', help ='urls to check', action='append')
        parser.add_argument('-info', '--information', dest = 'info', help = '%(prog)s Information Center', action='store_true')
        
        #   Parsing through the arguments
        arg = parser.parse_args()

        return arg

class SCChecker():

    '''
        Program Name : SiteConnectivity Checker
        Description : Checks site connectivity

        Developed by : @ krigjo25
        date :
    '''

    def ProgramInformation(self):

        '''
            #   Program information
            #   Program name, version, description

        '''

        name = '%(prog)s'
        version = '0.0.1'


        description = '''Checking connection for websites'''
        return sys.exit(f'Program name : {name}\nDescription : {description}Version : {version}')

    def PingConnection(self, urls):

        ''' Ping a internett connection'''

        for i in urls: p = ping(i, verbose=True)

        return

    def UrlParse(self, arg, mode, d = ','):

        '''
        
            #   Read given file
            #   Loop through the urls
        
        '''


        #   Opening up the document
        if mode == 'file':

            for i in arg:

                with open(i, 'r') as f:

                    try:

                        arg = f.read()
                        arg = arg.strip().split(f'{d}')

                        #   Iterating through the argument
                        for i in arg:

    #                        if not domaine in i: raise ValueError('Missing domaine')
                            if 'https://' not in i: i = f'https://{i}'.replace(' ', '')

                            req = r.get(i)
                            if req.status_code == 200: print(f'{req.url} is Online')
                            else: print(f'{req.url} Not found')

                        req.close()
                    except Exception as e: sys.exit('Missing domaine')
        else:

            try:

                if len(arg) > 1:

                    #   Fetch webpage
                    for i in arg:

                        #   Send a request to the page
                        req = r.get(i)

                        if req.status_code == 200: print(f'{req.url} is online')
                        else : print(f'{req.url} Not found')

                else:
                    for i in arg:
                        if 'https://' not in i: i = f'https://{i}'

                        req = r.get(i)
                        if req.status_code == 200 : print(f'{req.url} is Online')
                        else : print(f'{req.url} is offline')

            except Exception as e: sys.exit('Missing domaine')

            #   Close the request
            req.close()
        return

    def main(self):

        arg = CommandlineInterface().CommandLineOptions()

        try:

            if arg.info : return self.ProgramInformation()
            elif arg.inf: return self.UrlParse(arg.inf, mode ='file')
            elif arg.ping: return self.PingConnection(arg.ping)
            elif arg.urls: return self.UrlParse(arg.urls, mode = 'url')

        except Exception as e:sys.exit(e)
        return

if __name__ == '__main__':
    rp = SCChecker()
    rp.main()