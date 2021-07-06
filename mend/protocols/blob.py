from typing import Protocol


class Blob(Protocol):

    def read(self) -> bytes:
        raise NotImplementedError
