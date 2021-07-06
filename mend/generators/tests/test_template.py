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

    assert len(tree) == 1
    assert "foo" in tree

    blob = tree["foo"]
    data = blob.read().decode("utf-8")

    assert data == "baz"
