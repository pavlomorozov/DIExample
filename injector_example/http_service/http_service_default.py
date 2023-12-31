import requests
from injector import inject

from injector_example.http_service.http_service import HTTPService


class HTTPDefaultService(HTTPService):

    def __init__(self):
        pass

    def get_fundamentals(self, ticker):
        url = f'https://eodhd.com/api/fundamentals/{ticker}?api_token=demo'
        fundamentals_data = requests.get(url).json()
        return fundamentals_data
