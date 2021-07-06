from click import group

from mend.cli.generators import create_generator_commands


@group()
def main(*args, **kwargs) -> None:
    """
    Mend, update, and repair git respositories.

    """
    pass


create_generator_commands(main)
