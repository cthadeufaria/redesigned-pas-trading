"""Define and normalize information about different assets."""

from libraries.operations import operations

class Asset:
    """Class to define, control and receive information about indiivdual assets."""
    def __init__(self, ticker: str) -> None:
        self.ticker = ticker
        self.curr_price = operations.get_tickers['curr_price']
        self.max_price = price['max_price']
        self.min_price = price['min_price']