import inspect
from dataclasses import dataclass
from typing import Callable, Type, Dict, Generator, \
    Any

from .abstraction import AbstractServiceProvider, ServiceFactory, ServiceFactoryGenerator, TService
from .scope import ServiceScope


@dataclass
class ServiceInstance:
    value: Any

    def dispose(self):
        pass


@dataclass
class DisposableServiceInstance(ServiceInstance):
    def __init__(self, disposable: Generator):
        if not inspect.isgenerator(disposable):
            raise ValueError('expected a generator!')

        super().__init__(next(disposable))
        self._generator = disposable

    def dispose(self):
        try:
            next(self._generator)
        except StopIteration:
            pass
        except:
            raise


def create_service_instance(t: Type, s: AbstractServiceProvider, f: Callable, cleanup: Callable):
    x = f(t, s)
    if inspect.isgenerator(x):
        if isinstance(s, ServiceScope):
            s.on_dispose.append(cleanup)
        else:
            raise RuntimeError(
                'The service container does not support the scoping mechanism yet disposable services '
                'are being used!')

        return DisposableServiceInstance(x)
    else:
        return ServiceInstance(x)


def singleton(f: ServiceFactory[TService] | ServiceFactoryGenerator[TService]) -> ServiceFactory[TService]:
    instance: ServiceInstance | None = None

    def cleanup(*args):
        nonlocal instance
        if instance:
            instance.dispose()
            instance = None

    def wrapper(t: Type, s: AbstractServiceProvider):
        nonlocal instance
        if instance is None:
            instance = create_service_instance(t, s, f, cleanup)
        return instance.value

    return wrapper


def scoped(f: ServiceFactory[TService] | ServiceFactoryGenerator[TService]) -> ServiceFactory[TService]:
    instances: Dict[Any, ServiceInstance] = {}

    def cleanup(s: ServiceScope):
        nonlocal instances
        if instance := instances.get(s):
            instance.dispose()
        del instances[s]

    def wrapper(t: Type, s: AbstractServiceProvider):
        nonlocal instances
        if (instance := instances.get(s)) is None:
            instance = create_service_instance(t, s, f, cleanup)
            instances[s] = instance

        return instance.value

    return wrapper
