"""Control information and manages operations."""

from utils.api import Binance

class Operations:
    """Class to define, control and receive information about different assets."""
    def __init__(self, market = ['USDT']):
        # self.all_tickers = Binance.get_tickers(market)
        # self.history = Binance.get_history(self.all_tickers)

        # Create connection with Binance
        self.api = Binance()

    def get_tickers(self) -> None:
        self. tickers = self.api.get_tickers()