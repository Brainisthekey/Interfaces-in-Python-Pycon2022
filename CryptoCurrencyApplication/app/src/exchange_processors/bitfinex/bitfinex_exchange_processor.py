from datetime import datetime
from typing import ClassVar, Optional, Union
from src.exchange_processors.models import AccountDetails, CandleDetails, OrderDetails, ResponseDetails
from src.clients.bitfinex_client.bitfinex_client import BitfinexClient
from src.exchange_processors.exchange_processor import CryptoExchangeProcessor


class BitfinexExchangeProcessor(CryptoExchangeProcessor):

    url_path_check_connection: ClassVar[str] = 'v1/conn'
    url_path_to_get_candle: ClassVar[str] = "/v1/pubticker"
    url_path_to_get_order: ClassVar[str] = "/v1/order/"
    url_path_to_get_account_info: ClassVar[str] = "/v1/balances"

    def __init__(self, client: BitfinexClient):
        self.client = client
    
    def ping_client(self) -> ResponseDetails:
        ...

    def show_candles(self, symbol: str, interval: Optional[str]) -> Union[CandleDetails, ResponseDetails]:
        ...

    def place_order(self, symbol: str, side: str, type: str, quantity: float, price: float) -> Union[OrderDetails, ResponseDetails]:
        ...

    def get_account(self, timestamp: Optional[datetime]) -> Union[AccountDetails, ResponseDetails]:
        ...



