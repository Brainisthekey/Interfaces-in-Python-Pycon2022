from datetime import datetime
from typing import ClassVar, Optional, Union
from src.exchange_processors.models import AccountDetails, CandleDetails, OrderDetails, ResponseDetails
from src.clients.binance_client.binance_client import BinanceClient
from src.exchange_processors.exchange_processor import CryptoExchangeProcessor


class BinanceExchangeProcessor(CryptoExchangeProcessor):

    url_path_check_connection: ClassVar[str] = '/check_connection'
    url_path_to_get_candle: ClassVar[str] = "/klines"
    url_path_to_get_order: ClassVar[str] = "/order"
    url_path_to_get_account_info: ClassVar[str] = "/account"

    def __init__(self, client: BinanceClient):
        self.client = client
    
    def ping_client(self) -> ResponseDetails:
        ...

    def show_candles(self, symbol: str, interval: Optional[str]) -> Union[CandleDetails, ResponseDetails]:
        ...

    def place_order(self, symbol: str, side: str, type: str, quantity: float, price: float) -> Union[OrderDetails, ResponseDetails]:
        ...

    def get_account(self, timestamp: Optional[datetime]) -> Union[AccountDetails, ResponseDetails]:
        ...
