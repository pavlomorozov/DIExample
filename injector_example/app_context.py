from injector import Injector, Module

from injector_example.http_service.http_service import HTTPService
from injector_example.http_service.http_service_default import HTTPDefaultService
from injector_example.http_service.http_service_development import HTTPDevelopmentService
from injector_example.processor_service import ProcessorService
from injector_example.profiles import Profiles


class ApplicationContext:

    def __init__(self, profile):
        self.__injector = Injector()
        self.__profile = profile

        # The HTTPService implementation defined by profile
        if Profiles.DEFAULT == profile:
            self.__injector.binder.bind(HTTPService, HTTPDefaultService)
        if Profiles.DEVELOPMENT == profile:
            self.__injector.binder.bind(HTTPService, HTTPDevelopmentService)

        self.__processor_service = self.__injector.get(ProcessorService)

    def run(self):
        self.__processor_service.run()
