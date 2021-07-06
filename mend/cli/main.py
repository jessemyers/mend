from pkg_resources import get_entry_map
from typing import Type

from click import Choice, command, option

from mend.protocols import Generator, Plugin


GENERATORS: dict[str, Type[Generator]] = {
    key: module.load()
    for key, module in get_entry_map("mend", "mend.generators").items()
}


PLUGINS: dict[str, Type[Plugin]] = {
    key: module.load()
    for key, module in get_entry_map("mend", "mend.plugins").items()
}


def get_generator(context, param, value: str) -> Generator:
    return GENERATORS[value]()


def get_plugin(context, param, value: str) -> Plugin:
    return PLUGINS[value]()


@command()
@option(
    "--generator",
    "-g",
    callback=get_generator,
    default="hello",
    type=Choice(list(GENERATORS.keys())),
)
@option(
    "--plugin",
    "-p",
    callback=get_plugin,
    default="echo",
    type=Choice(list(PLUGINS.keys())),
)
def main(*, generator: Generator, plugin: Plugin, **kwargs) -> None:
    plugin.mend(generator.generate())
