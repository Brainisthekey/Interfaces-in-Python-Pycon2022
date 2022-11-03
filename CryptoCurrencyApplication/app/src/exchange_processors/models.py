from typing import Any
from pydantic import BaseModel


class CandleDetails(BaseModel):
    """
    Model representing Candle

    `symbol`: str
        Symbol of candle

    `price`: str
        Current price of pair
    """
    symbol: str
    price: str


class OrderDetails(BaseModel):
    """
    The Order details

    `status`: str
        Order status

    `ticker`: str
        Price of opened/closed/moved position
    """
    status: str
    ticker: str

class AccountDetails(BaseModel):
    """
    Get account info
    
    `username`: str
        The username of account

    `balance`: dict[str, Any]
        Balance pair - {'BTC': 1.00}
    """
    username: str
    balances: dict[str, Any]

class ResponseDetails(BaseModel):
    """Detail of request"""
    request_url: str
    status_code: int
    details: str
