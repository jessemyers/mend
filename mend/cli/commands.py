from typing import Callable, Type, TypeVar

from click import Command

from mend.protocols import WithParameters


C = TypeVar("C", bound=WithParameters)


def add_parameters(cls: Type[C], command: Command) -> None:
    for parameter in cls.iter_parameters():
        command.params.append(parameter)


def create_from_parameters(cls: Type[C]) -> Callable[..., C]:
    def func(**kwargs) -> C:
        return cls.from_parameters(**kwargs)

    func.__doc__ = cls.__doc__

    return func
