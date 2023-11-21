from injector import Injector, Module

from injector_example.http_service.http_service import HTTPService
from injector_example.http_service.http_service_default import HTTPDefaultService
from injector_example.http_service.http_service_development import HTTPDevelopmentService
from injector_example.processor_service import ProcessorService
from injector_example.profiles import Profiles


class ApplicationContext:

    def __init__(self, profile):
        # Injector instance initiated
        self.__injector = Injector()
        # Profile value can be bound to Injector and later injected while creating managed classes instances.
        self.__injector.binder.bind(Profiles, profile)

        # The HTTPService implementation defined by profile. This done with binding the HTTPService implementation.
        if Profiles.DEFAULT == profile:
            self.__injector.binder.bind(HTTPService, HTTPDefaultService)
        if Profiles.DEVELOPMENT == profile:
            self.__injector.binder.bind(HTTPService, HTTPDevelopmentService)

        # Injector does not need explicit binding here because we have just one ProcessorService class
        self.__processor_service = self.__injector.get(ProcessorService)

    def run(self):
        self.__processor_service.run()
