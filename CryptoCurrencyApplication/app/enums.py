from enum import Enum


class ExchangeTypes(Enum):
    BINANCE = 'binance'
    BITFINEX = 'bitfinex'


class ActionTypes(Enum):
    GET_ACCOUNT = 'get_account'
    GET_CANDLE = 'get_candle'
    PLACE_ORDER = 'place_order'