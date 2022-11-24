"""Define, control and receive information about different assets."""

from utils.api import Binance

class Asset:
    """Class to define, control and receive information about different assets."""
    def __init__(self, ticker):
        self.ticker = ticker

    def info(self):
        self.datetime = Binance.get_history(self.ticker)
        