"""Control information and manages operations."""

from utils.api import Binance

class Manager:
    """Class to define, control and receive information about different assets."""
    def __init__(self, market: list = 'USDT'):
        self.all_tickers = Binance.get_tickers(market)
        self.history = Binance.get_history(self.all_tickers)