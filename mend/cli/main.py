from click import group

from mend.cli.generators import create_generator_commands
from mend.cli.plugins import create_plugin_option
from mend.protocols import Generator, Plugin


@group()
def main(*args, **kwargs) -> None:
    """
    Mend, update, and repair git respositories.

    """
    pass


create_plugin_option(main)
create_generator_commands(main)


@main.result_callback()
def execute(generator: Generator, *args, plugin: Plugin, **kwargs):
    tree = generator.generate()
    plugin.mend(tree)
