from dataclasses import dataclass
from typing import BinaryIO, Iterable, Type

from click import Argument, Parameter, Path

from mend.protocols import Generator, Tree


@dataclass(frozen=True)
class FileGenerator(Generator):
    """
    Generate from a local file.

    """
    blob: BinaryIO
    name: str
    path: str

    def close(self) -> None:
        self.blob.close()

    def generate(self) -> Tree:
        return {
            self.name: self.blob,
        }

    @classmethod
    def iter_parameters(cls: Type["FileGenerator"]) -> Iterable[Parameter]:
        yield Argument(
            [
                "path",
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
            cls: Type["FileGenerator"],
            *args,
            **kwargs,
    ) -> "FileGenerator":
        path = kwargs["path"]

        return cls(
            blob=open(path, "rb"),
            name="file",
            path=path,
        )
