"""This is root of package."""

from atsphinx.helper.decorators import emit_only
from bs4 import BeautifulSoup
from sphinx.application import Sphinx
from sphinx.jinja2glue import BuiltinTemplateLoader

__version__ = "0.1.4"


class WithHtmxTemplateLoader(BuiltinTemplateLoader):  # noqa: D101
    def render(self, template: str, context: dict) -> str:  # noqa: D102
        out = super().render(template, context)
        if not template.endswith(".html"):
            return out
        soup = BeautifulSoup(out, "html.parser")
        soup.body["hx-boost"] = "true"
        for form in soup.find_all("form"):
            form["hx-boost"] = "false"
        return soup.prettify()


@emit_only(formats=["html"])
def setup_custom_loader(app: Sphinx):
    """Inject extra values about htmx-boost into generated config."""
    app.config.template_bridge = "atsphinx.htmx_boost.WithHtmxTemplateLoader"
    app.builder.init()
    app.builder.add_js_file("https://unpkg.com/htmx.org@1.9.10")


def setup(app: Sphinx):
    """Load as Sphinx-extension."""
    app.connect("builder-inited", setup_custom_loader)
    return {
        "version": __version__,
        "env_version": 1,
        "paralell_read_safe": True,
    }
