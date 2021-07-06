from dataclasses import dataclass
from difflib import unified_diff
from typing import Iterable, Optional, Type

from click import (
    Option,
    Parameter,
    Path,
    echo,
    style,
)

from mend.protocols import Blob, Plugin, Tree


@dataclass(frozen=True)
class DiffPlugin(Plugin):
    """
    Calculate difference between generated source and path.

    """
    name: str
    path: str

    def mend(self, tree: Tree) -> None:
        with open(self.path, "rb") as left:
            right = tree.get(self.name)
            for item in self.diff(self.name, left, right):
                echo(item.strip("\n"))

    def diff(self, name: str, left: Optional[Blob], right: Optional[Blob]) -> Iterable[str]:
        """
        Produce a single file diff, assuming text data.

        """
        left_lines = left.read().decode("utf-8").splitlines() if left else []
        right_lines = right.read().decode("utf-8").splitlines() if right else []
        left_name = f"{name} - generated"
        right_name = f"{name} - original"

        lines = unified_diff(left_lines, right_lines, left_name, right_name, lineterm="")

        for line in lines:
            if line.startswith("+"):
                yield style(line, fg="green")
            elif line.startswith("-"):
                yield style(line, fg="red")
            elif line.startswith("@"):
                yield style(line, fg="blue")
            else:
                yield line

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
            name="file",
        )
