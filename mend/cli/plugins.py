from pkg_resources import get_entry_map

from click import Group

from mend.cli.commands import add_parameters, create_from_parameters


def create_plugin_commands(parent: Group) -> None:
    for key, module in get_entry_map("mend", "mend.plugins").items():
        cls = module.load()
        func = create_from_parameters(cls)
        command = parent.command(key)(func)
        add_parameters(cls, command)
