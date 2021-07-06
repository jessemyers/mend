from typing import Protocol

from mend.protocols.tree import Tree


class Plugin(Protocol):

    def mend(self, tree: Tree) -> None:
        raise NotImplementedError
