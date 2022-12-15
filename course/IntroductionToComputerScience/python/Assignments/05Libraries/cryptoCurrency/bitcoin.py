#   Importing Resposories
import sys
import json
import requests

def BitCoin():

        '''
            #   Author : krigjo25
            #   Date :  23.09-22

            #   Expect the user to specify as a command-line argument the number of Bitcoins, n, that they would like to purchase.
            #   If the argument can not be floated. Exit the program.

            #   Queries the API for the CoinDesk Bitcoin Price Index at api.coindesk.com/v1/bpi/currentprice.json
                Returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
            #   Catch any exceptions.
            #   Outputs the current cost n Bitcoins in USD to four decimal places, using ", " as seperator.
        '''

        #   Initializing Classes
        res = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        jsonData = json.loads(res.text)

        try:

            if sys.argv[1]: Dcoin = float(sys.argv[1])

        except Exception as e:
            sys.exit(e)

        else:

            #   Retrieve the ammount of one bitcoin
            usd = jsonData['bpi']['USD']['rate_float']

            # Calculating the exchangerate
            usd *= Dcoin

            print(f'${usd:,.4f}')

BitCoin()