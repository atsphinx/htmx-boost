"""This is root of package."""

from sphinx.application import Sphinx

__version__ = "0.0.0"


def setup(app: Sphinx):
    """Load as Sphinx-extension."""
    return {
        "version": __version__,
        "env_version": 1,
        "paralell_read_safe": True,
    }
