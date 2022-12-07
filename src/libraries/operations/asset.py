"""Define and normalize information about different assets."""

from utils.api import Binance
from libraries.operations import manager

class Asset:
    """Class to define, control and receive information about different assets."""
    def __init__(self, ticker) -> None:
        self.ticker = ticker
        self.curr_price = Binance.get_tickers['curr_price']
        self.max_price = price['max_price']
        self.min_price = price['min_price']