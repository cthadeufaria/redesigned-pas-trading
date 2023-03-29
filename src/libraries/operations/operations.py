"""Control information and manages operations."""

from utils.api import Binance
from controller import PID
import model as RuizCruz

class Operations:
    """Class to control and receive information about different assets, update the mathematical model and call controller strategy to update portfolio."""
    def __init__(self, market = ['USDT']):
        # self.all_tickers = Binance.get_tickers(market)
        # self.history = Binance.get_history(self.all_tickers)

        # Create connection with Binance
        # self.api = Binance()
        pass


    def create_model(self) -> None:
        self.tickers = self.api.get_tickers()
