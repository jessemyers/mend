from pathlib import Path

from jinja2 import DictLoader

from mend.generators.template import TemplateGenerator


def test_template_generator() -> None:
    generator = TemplateGenerator(
        loader=DictLoader(dict(
            foo="{{ bar }}",
        )),
        context=dict(
            bar="baz",
        ),
    )

    tree = generator.generate()

    assert len(tree.blobs) == 1
    assert Path("foo") in tree.blobs

    blob = tree.blobs[Path("foo")]
    data = blob.read().decode("utf-8")

    assert data == "baz"
