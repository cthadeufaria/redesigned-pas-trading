"""Control api connections and information gathering."""
import os
import requests
from constants.endpoints import endpoints
from typing import Tuple, Optional

class Binance:
    """Class to manage connection with Binance and data retrieving and inputting."""
    def __init__(self, api_type: str = 'prod', endpoints = endpoints):
        self.auth: Tuple[Optional[str], Optional[str]]
        self.endpoints = endpoints
        self.api_type = api_type

        if self.api_type == 'test':
            self.main_endpoint = 'https://testnet.binance.vision'
            self.auth_dict = {
                'key' : os.environ.get('TEST_KEY'),
                'skey' : os.environ.get('TEST_SKEY'),
            }
        elif self.api_type == 'prod':
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
            print('Could not ping Binance API.')

    def get_tickers(self, market: str = 'USDT') -> list[str]:
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