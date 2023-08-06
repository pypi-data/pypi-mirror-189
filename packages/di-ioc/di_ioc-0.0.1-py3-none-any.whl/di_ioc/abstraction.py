from abc import ABC, abstractmethod
from typing import Callable, Type, TypeVar, Optional, ContextManager, Generator, \
    Hashable, Self, MutableMapping

TService = TypeVar('TService')


class AbstractServiceProvider(Hashable, ContextManager[Self], ABC):
    @abstractmethod
    def get_service(self, service_type: Type[TService]) -> Optional[TService]: ...

    @abstractmethod
    def get_required_service(self, service_type: Type[TService]) -> TService: ...

    @abstractmethod
    def create_scope(self) -> Self: ...


DisposableServiceInstance = Generator[TService, None, None]
ServiceFactory = Callable[[Type[TService], AbstractServiceProvider], TService]
ServiceFactoryGenerator = Callable[[Type[TService], AbstractServiceProvider], DisposableServiceInstance[TService]]


class AbstractServiceContainer(MutableMapping[Type, ServiceFactory], ABC):

    @abstractmethod
    def register(self, *other: 'AbstractServiceContainer'): ...
