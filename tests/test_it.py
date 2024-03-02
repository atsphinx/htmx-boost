"""Standard integration tests."""

from io import StringIO

import pytest
from bs4 import BeautifulSoup
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html")
def test__it(app: SphinxTestApp, status: StringIO, warning: StringIO):
    """Test to pass."""


@pytest.mark.sphinx("html", confoverrides={"html_theme": "alabaster"})
def test__work_on_bundle_theme(app: SphinxTestApp):
    app.build()
    soup = BeautifulSoup((app.outdir / "index.html").read_text(), "html.parser")
    assert "hx-boost" in soup.body.attrs


@pytest.mark.sphinx("html", confoverrides={"html_theme": "furo"})
def test__work_on_custom_theme_1(app: SphinxTestApp):
    app.build()
    soup = BeautifulSoup((app.outdir / "index.html").read_text(), "html.parser")
    assert "hx-boost" in soup.body.attrs


@pytest.mark.sphinx("html", confoverrides={"html_theme": "sphinx_rtd_theme"})
def test__work_on_custom_theme_2(app: SphinxTestApp):
    app.build()
    soup = BeautifulSoup((app.outdir / "index.html").read_text(), "html.parser")
    assert "hx-boost" in soup.body.attrs
