import json
from injector import inject

from injector_example.http_service.http_service import HTTPService


class HTTPDevelopmentService(HTTPService):

    def __init__(self):
        filename = 'injector_example/http_service/response_samples/fundamentals_development.json'
        f = open(filename)
        self.__fundamentals_data = json.load(f)

    def get_fundamentals(self, ticker):
        return self.__fundamentals_data
