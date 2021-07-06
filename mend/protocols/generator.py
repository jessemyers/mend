from typing import Protocol

from mend.protocols.tree import Tree


class Generator(Protocol):

    def generate(self) -> Tree:
        raise NotImplementedError
