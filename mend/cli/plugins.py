from pkg_resources import get_entry_map
from typing import Type

from click import Choice, Group, Option

from mend.protocols import Plugin


def create_plugin_option(group: Group) -> None:
    """
    Attach the "--plugin" option.

    """
    plugins: dict[str, Type[Plugin]] = {
        key: module.load()
        for key, module in get_entry_map("mend", "mend.plugins").items()
    }

    option = Option(
        [
            "--plugin",
            "-p",
        ],
        callback=lambda context, param, value: plugins[value](),
        default="echo",
        type=Choice(list(plugins.keys())),
    )

    group.params.append(option)
