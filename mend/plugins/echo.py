from click import echo

from mend.protocols import Plugin, Tree


class EchoPlugin(Plugin):
    """
    Echo generated source.

    """
    def mend(self, tree: Tree) -> None:
        for key in tree:
            echo(key)
