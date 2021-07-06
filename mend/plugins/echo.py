from click import echo

from mend.protocols import Plugin, Tree


class Echo(Plugin):

    def mend(self, tree: Tree) -> None:
        for key in tree:
            echo(key)

    # TODO
