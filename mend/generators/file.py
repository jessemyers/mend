from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Type

from click import (
    Argument,
    Option,
    Parameter,
    Path as PathType,
)

from mend.files import FileBlob
from mend.protocols import Generator, Tree


@dataclass(frozen=True)
class FileGenerator(Generator):
    """
    Generate from a local file.

    """
    blob: FileBlob

    def close(self) -> None:
        self.blob.close()

    def generate(self) -> Tree:
        return self.blob.as_tree()

    @classmethod
    def iter_parameters(cls: Type["FileGenerator"]) -> Iterable[Parameter]:
        yield Option(
            [
                "--use-path-as-name",
                "-u",
            ],
            is_flag=True,
        )
        yield Argument(
            [
                "path",
            ],
            required=True,
            type=PathType(
                allow_dash=False,
                dir_okay=False,
                exists=True,
                file_okay=True,
                path_type=Path,
                readable=True,
                resolve_path=True,
                writable=False,
            ),
        )

    @classmethod
    def from_parameters(
            cls: Type["FileGenerator"],
            *args,
            **kwargs,
    ) -> "FileGenerator":
        use_path_as_name = kwargs["use_path_as_name"]
        path = kwargs["path"]

        return cls(
            blob=FileBlob.open(
                path=path,
                name=path if use_path_as_name else "file",
            ),
        )
