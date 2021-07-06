from io import BytesIO

from mend.protocols import Generator, Tree


class Hello(Generator):

    def generate(self) -> Tree:
        return dict(
            hello=BytesIO("world".encode("utf-8")),
        )
