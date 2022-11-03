import click
import requests
from datetime import datetime
from src.clients.binance_client.binance_client import BinanceClient
from src.clients.bitfinex_client.bitfinex_client import BitfinexClient
from src.exchange_processors.binance.binance_exchange_processor import BinanceExchangeProcessor
from src.exchange_processors.bitfinex.bitfinex_exchange_processor import BitfinexExchangeProcessor
from enums import ExchangeTypes, ActionTypes


@click.command()
@click.option(
    '--exchange',
    required=True,
    type=click.Choice(['binance', 'bitfinex']),
    help='Exchange platform'
)
@click.option('--secret_key', required=True, help='Secret key')
def request_client(exchange, secret_key):
    match exchange:
        case ExchangeTypes.BINANCE.value:
            exchange_processor: BinanceExchangeProcessor = BinanceExchangeProcessor(BinanceClient(secret_key))
        case ExchangeTypes.BITFINEX.value:
            exchange_processor: BitfinexExchangeProcessor = BitfinexExchangeProcessor(BitfinexClient(secret_key))
    
    if not exchange_processor.ping_client().status_code == requests.codes.OK:
        click.echo(click.style('Client is not authorized, please check secret key', fg='red'))
        return

    click.echo(click.style('Successfully authorize the client', fg='green'))
    while True:
        action = click.prompt('Which action do you want to perform - [get_account | get_candle | place_order] ')
        if action == ActionTypes.GET_ACCOUNT.value:
            params = click.prompt('Please provide the data in following format: dd/mm/yyyy ')
            date = datetime.strptime(params.rstrip(), '%d/%m/%Y').date()
            result = exchange_processor.get_account(date)
            click.echo(click.style(result, fg='green'))
        if action == ActionTypes.PLACE_ORDER.value:
            ...


if __name__ == "__main__":
    request_client()
