from atsphinx.htmx_boost import __version__

# -- Project information
project = "atsphinx-htmx-boost"
copyright = "2024, Kazuya Takei"
author = "Kazuya Takei"
release = __version__

# -- General configuration
extensions = ["atsphinx.htmx_boost", "sphinx.ext.githubpages"]
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "furo"
html_title = f"{project} v{release}"
html_static_path = ["_static"]

# -- Options for extensions
# For atsphinx.htmx_boost
htmx_boost_preload = "mouseover"
