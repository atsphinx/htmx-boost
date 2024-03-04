"""This is root of package."""

from bs4 import BeautifulSoup
from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.jinja2glue import BuiltinTemplateLoader

__version__ = "0.1.3"


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


def setup_custom_loader(app: Sphinx, config: Config):
    """Inject extra values about htmx-boost into generated config."""
    # TODO: This extension must be loaded with html builders.
    config.template_bridge = "atsphinx.htmx_boost.WithHtmxTemplateLoader"
    if not hasattr(config, "html_js_files"):
        config.html_js_files = []
    # NOTE: Need control by config value?
    config.html_js_files.append("https://unpkg.com/htmx.org@1.9.10")


def setup(app: Sphinx):
    """Load as Sphinx-extension."""
    app.connect("config-inited", setup_custom_loader)
    return {
        "version": __version__,
        "env_version": 1,
        "paralell_read_safe": True,
    }
