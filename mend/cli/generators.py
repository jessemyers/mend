from pkg_resources import get_entry_map
from typing import Type

from click import Command, Group

from mend.protocols import Generator


def create_generator_command(
        name: str,
        generator_cls: Type[Generator],
        group: Group,
) -> Command:
    """
    Create a `click` command for a `Generator` and attach it to the provided `group`.

    """
    def _command(**kwargs) -> Generator:
        return generator_cls.from_parameters(**kwargs)

    _command.__doc__ = generator_cls.__doc__
    _command.__name__ = name

    command = group.command(name)(_command)

    for parameter in generator_cls.iter_parameters():
        command.params.append(parameter)

    return command


def create_generator_commands(
        group: Group,
) -> None:

    generators: dict[str, Type[Generator]] = {
        key: module.load()
        for key, module in get_entry_map("mend", "mend.generators").items()
    }

    for name, generator_cls in generators.items():
        create_generator_command(name, generator_cls, group)
