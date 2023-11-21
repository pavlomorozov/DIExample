from injector import inject

from injector_example.http_service.http_service import HTTPService


class ProcessorService:

    @inject
    def __init__(self, http_service: HTTPService):
        self.__http_service = http_service

    def run(self):
        # AAPL ticker represents Apple company
        fundamentals_json = self.__http_service.get_fundamentals('AAPL')
        # DeveloperNote attribute defined with development profile
        developer_note = fundamentals_json.get('DeveloperNote')
        print(f'Fundamentals data DeveloperNote: {developer_note}')
