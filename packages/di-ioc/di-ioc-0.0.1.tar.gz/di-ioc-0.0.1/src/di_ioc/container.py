import logging
from typing import Type, Optional, Mapping, Iterator, ChainMap, Self

from .abstraction import AbstractServiceContainer, AbstractServiceProvider, ServiceFactory, TService
from .scope import ServiceScope

log = logging.getLogger(__name__)


class ServiceContainer(AbstractServiceContainer, AbstractServiceProvider, ServiceScope):

    def __init__(self, *factories: Mapping[Type, ServiceFactory]):
        super().__init__()
        self._registry = ChainMap[Type, ServiceFactory]({}, *factories)

    def __hash__(self) -> int:
        return id(self)

    def __getitem__(self, service_type: Type[TService]) -> ServiceFactory[TService]:
        return self._registry[service_type]

    def __setitem__(self, service_type: Type[TService], service_factory: ServiceFactory[TService]) -> None:
        self._registry[service_type] = service_factory

    def __delitem__(self, service_type: Type) -> None:
        del self._registry[service_type]

    def __len__(self) -> int:
        return len(self._registry)

    def __iter__(self) -> Iterator[Type]:
        return iter(self._registry)

    def __enter__(self) -> Self:
        log.debug('entered service scope')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dispose()
        log.debug('exited service scope')

    def get_service(self, service_type: Type[TService]) -> Optional[TService]:
        if issubclass(service_type, AbstractServiceProvider):
            return self.create_scope()

        return service_factory(service_type, self) \
            if (service_factory := self._registry.get(service_type, None)) \
            else None

    def get_required_service(self, service_type: Type[TService]) -> TService:
        service = self.get_service(service_type)
        if service is None:
            raise ValueError(f'required service {service_type.__name__} is not registered.')
        return service

    def register(self, *other: AbstractServiceContainer):
        self._registry.maps.extend(other)

    def create_scope(self) -> Self:
        return ServiceContainer(self._registry)
