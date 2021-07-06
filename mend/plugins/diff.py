from dataclasses import dataclass
from typing import Iterable, Type

from click import (
    Option,
    Parameter,
    Path,
    echo,
)

from mend.protocols import Plugin, Tree


@dataclass(frozen=True)
class DiffPlugin(Plugin):
    """
    Calculate difference between generated source and path.

    """
    path: str

    def mend(self, tree: Tree) -> None:
        echo("Not implemented")

    @classmethod
    def iter_parameters(cls: Type["DiffPlugin"]) -> Iterable[Parameter]:
        yield Option(
            [
                "--path",
            ],
            required=True,
            type=Path(
                allow_dash=False,
                dir_okay=False,
                exists=True,
                file_okay=True,
                path_type=str,
                readable=True,
                resolve_path=True,
                writable=False,
            ),
        )

    @classmethod
    def from_parameters(
            cls: Type["DiffPlugin"],
            *args,
            **kwargs,
    ) -> "DiffPlugin":
        path = kwargs["path"]

        return cls(
            path=path,
        )
