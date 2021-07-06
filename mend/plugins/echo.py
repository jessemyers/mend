from click import echo, style

from mend.protocols import Plugin, Tree


class EchoPlugin(Plugin):
    """
    Echo generated source.

    """
    def mend(self, tree: Tree) -> None:
        for name, blob in tree.items():
            echo(style(f"# {name}", fg="green"))
            lines = blob.read().decode("utf-8").splitlines()
            for line in lines:
                echo(line)
