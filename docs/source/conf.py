# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# Don't allow Kivy to handle args
os.environ["KIVY_NO_ARGS"] = "1"

from sphinx.application import Sphinx
from sphinx.highlighting import lexers
from sphinx.util.docfields import Field
from sphinxawesome_theme.postprocess import Icons

os.environ["READTHEDOCS"] = "true"

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("../../."))

from _extensions.kivy_lexer import KivyLexer

from carbonkivy import __version__

# Register the lexer with Sphinx
lexers["kv"] = KivyLexer()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "CarbonKivy"
copyright = '2025, "Kartavya Shukla"'
author = '"Kartavya Shukla"'
version = __version__
release = __version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "autoapi.extension",
    "sphinx_design",
    "sphinxext.opengraph",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinxawesome_theme",
]
master_doc = "index"
autodoc_mock_imports = ["kivy"]
templates_path = ["_templates"]
exclude_patterns = []
extlinks = {
    "gh": ("https://github.com/CarbonKivy/CarbonKivy/blob/master/%s", "%s"),
    "ghdir": ("https://github.com/CarbonKivy/CarbonKivy/tree/master/%s", "%s"),
    "kivy": ("https://kivy.org/%s", "%s"),
}

# -- Autoapi configuration ---------------------------------------------------

autoapi_dirs = ["../../carbonkivy"]
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
]
autoapi_file_patterns = ["*.py"]
autoapi_type = "python"
autoapi_generate_api_docs = True
autoapi_keep_files = False

# -- Options for opengraph ---------------------------------------------------

ogp_site_url = "https://carbonkivy.readthedocs.io"
ogp_site_name = "CarbonKivy Documentation"
ogp_image = "/_static/images/carbonkivy_banner512.png"
ogp_custom_tags = [
    "<meta property='og:title' content='CarbonKivy - Carbon Design Kivy'/>",
    "<meta property='og:description' content='CarbonKivy is a Python library that integrates IBM's Carbon Design System with the Kivy framework.'/>",
    "<meta property='og:type' content='website'/>",
    "<meta property='keywords' content='CarbonKivy, Carbon, Design, System, Kivy, Python, Android, iOS, Windows, Linux, macOS'/>",
    "<meta property='description' content='CarbonKivy is a Python library that integrates IBM's Carbon Design System with the Kivy framework.'/>",
]

# -- Options for Code Highlighting -------------------------------------------

pygments_style = "sphinx"
pygments_style_dark = "dracula"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinxawesome_theme"
html_favicon = "_static/images/carbonkivy_logo128.png"
html_permalinks_icon = Icons.permalinks_icon
html_theme_options = {
    "logo_light": "_static/images/carbonkivy_logo64.png",
    "logo_dark": "_static/images/carbonkivy_logo_dark64.png",
    "show_breadcrumbs": True,
    "show_prev_next": True,
    "awesome_external_links": True,
    "extra_header_link_icons": {
        "GitHub": {
            "link": "https://github.com/CarbonKivy/CarbonKivy",
            "icon": (
                '<svg height="26px" style="margin-top:-2px;display:inline" '
                'viewBox="0 0 45 44" '
                'fill="currentColor" xmlns="http://www.w3.org/2000/svg">'
                '<path fill-rule="evenodd" clip-rule="evenodd" '
                'd="M22.477.927C10.485.927.76 10.65.76 22.647c0 9.596 6.223 17.736 '
                "14.853 20.608 1.087.2 1.483-.47 1.483-1.047 "
                "0-.516-.019-1.881-.03-3.693-6.04 "
                "1.312-7.315-2.912-7.315-2.912-.988-2.51-2.412-3.178-2.412-3.178-1.972-1.346.149-1.32.149-1.32 "  # noqa
                "2.18.154 3.327 2.24 3.327 2.24 1.937 3.318 5.084 2.36 6.321 "
                "1.803.197-1.403.759-2.36 "
                "1.379-2.903-4.823-.548-9.894-2.412-9.894-10.734 "
                "0-2.37.847-4.31 2.236-5.828-.224-.55-.969-2.759.214-5.748 0 0 "
                "1.822-.584 5.972 2.226 "
                "1.732-.482 3.59-.722 5.437-.732 1.845.01 3.703.25 5.437.732 "
                "4.147-2.81 5.967-2.226 "
                "5.967-2.226 1.185 2.99.44 5.198.217 5.748 1.392 1.517 2.232 3.457 "
                "2.232 5.828 0 "
                "8.344-5.078 10.18-9.916 10.717.779.67 1.474 1.996 1.474 4.021 0 "
                "2.904-.027 5.247-.027 "
                "5.96 0 .58.392 1.256 1.493 1.044C37.981 40.375 44.2 32.24 44.2 "
                '22.647c0-11.996-9.726-21.72-21.722-21.72" '
                'fill="currentColor"/></svg>'
            ),
        },
    },
}
html_static_path = ["_static"]
html_css_files = ["css/root.css"]


# -- Register a :confval: interpreted text role ----------------------------------
def setup(app: Sphinx) -> None:
    """Register the ``confval`` role and directive.

    This allows to declare theme options as their own object
    for styling and cross-referencing.
    """
    app.add_object_type(
        "confval",
        "confval",
        objname="configuration parameter",
        doc_field_types=[
            Field(
                "default",
                label="default",
                has_arg=True,
                names=("default",),
                bodyrolename="class",
            )
        ],
    )


intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "kivy": ("https://kivy.org/doc/master", None),
}
