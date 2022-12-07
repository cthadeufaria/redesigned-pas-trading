"""Control api connections and information gathering."""
import os
import requests
from constants.endpoints import endpoints

class Binance:
    """Class to connect with Binance."""
    def __init__(self, api_type: str = 'prod', endpoints = endpoints):
        self.endpoints = endpoints

        if api_type == 'test':
            self.main_endpoint = 'https://testnet.binance.vision'
            self.auth_dict = {
                'key' : os.environ.get('TEST_KEY'),
                'skey' : os.environ.get('TEST_SKEY'),
            }
        elif api_type == 'prod':
            self.main_endpoint = 'https://api1.binance.com'
            self.options_endpoint = 'https://vapi.binance.com'
            self.auth_dict = {
                'key' : os.environ.get('SPOT_KEY'),
                'skey' : os.environ.get('SPOT_SKEY'),
            }

        # Complete endpoints strings.
        for i in self.endpoints:
            if i[0:7] == 'options':
                self.endpoints[i] = self.options_endpoint + self.endpoints[i]
            else:
                self.endpoints[i] = self.main_endpoint + self.endpoints[i]
            
        print(self.endpoints)

        try:
            r = requests.get(endpoints['test'])
            print('ping: ' + str(r) + '\nConnection successful')
        except:
            print('Could not ping API.')

    def get_tickers(self, market: str) -> list[str]:
        r1 = requests.get(endpoints['exchange_info'], auth=(self.auth_dict['key'], self.auth_dict['skey']))
        tickers: list
        tickers = []
        for i in range(0, len(r1.json()['symbols'])):
            if r1.json()['symbols'][1]['status'] == 'TRADING':
                if r1.json()['symbols'][i]['quoteAsset'] == market:
                    tickers.append(r1.json()['symbols'][i]['symbol'])
                elif market == None:
                    tickers.append(r1.json()['symbols'][i]['symbol'])
        print(tickers)

        return tickers