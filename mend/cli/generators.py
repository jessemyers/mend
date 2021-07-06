from pkg_resources import get_entry_map

from click import Group

from mend.cli.commands import add_parameters
from mend.cli.plugins import create_plugin_commands
from mend.protocols import Plugin


def noop(**kwargs):
    pass


def create_generator_commands(parent: Group) -> None:
    for key, module in get_entry_map("mend", "mend.generators").items():

        cls = module.load()
        group = parent.group(key)(noop)
        add_parameters(cls, group)

        create_plugin_commands(group)

        @group.result_callback()
        def execute(plugin: Plugin, **kwargs):
            generator = cls.from_parameters(**kwargs)
            tree = generator.generate()
            plugin.mend(tree)
