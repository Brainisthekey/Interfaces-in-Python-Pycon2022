from abc import ABC, abstractmethod
from typing import Optional, TypeVar, Union
from src.clients.http_client import HTTPClient
from src.exchange_processors.models import CandleDetails, AccountDetails, OrderDetails, ResponseDetails
from datetime import datetime


Client = TypeVar('Client', bound=HTTPClient)


class CryptoExchangeProcessor(ABC):
    """Crypto Exchange processor"""

    @abstractmethod
    def __init__(self, client: Client) -> None:
        """Initialization of the client"""
        self.client: Client = client

    @classmethod
    @property
    @abstractmethod
    def url_path_check_connection(cls) -> str:
        """Check connection"""
        raise NotImplementedError()

    @classmethod
    @property
    @abstractmethod
    def url_path_to_get_candle(cls) -> str:
        """Path to get information about candle"""
        raise NotImplementedError()

    @classmethod
    @property
    @abstractmethod
    def url_path_to_get_order(cls) -> str:
        """Path to get/put order"""
        raise NotImplementedError()

    @classmethod
    @property
    @abstractmethod
    def url_path_to_get_account_info(cls) -> str:
        """Path to get account information"""
        raise NotImplementedError()

    @abstractmethod
    def ping_client(self) -> ResponseDetails:
        """Ping client in order to check connection"""
        raise NotImplementedError()

    @abstractmethod
    def show_candles(
        self,
        symbol: str,
        interval: Optional[str],
    ) -> Union[CandleDetails, ResponseDetails]:
        """Show information about the candles"""
        raise NotImplementedError()

    @abstractmethod
    def place_order(
        self,
        symbol: str,
        side: str,
        type: str,
        quantity: float,
        price: float,
    ) -> Union[OrderDetails, ResponseDetails]:
        """Place order"""
        raise NotImplementedError()

    @abstractmethod
    def get_account(
        self,
        timestamp: Optional[datetime],
    ) -> Union[AccountDetails, ResponseDetails]:
        """Get account information"""
        raise NotImplementedError()
